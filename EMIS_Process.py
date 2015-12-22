
import sys, csv, datetime, pprint
from Recon_line_spec import *


# TODO: verify EMIS RECON file integrity
# Current implementation is based on no corruption on EMIS Transaction Reconciliation File



def process_line (line_content, line_spec):
	line_info = dict()
	for field in line_spec:
		field_name = field["Name"]
		field_content = line_content[field["Start Pos."] - 1: field["Start Pos."]  + field["Length"] - 1]
		if field["Format"] == "Default":
			line_info[field_name] = field_content
		if field["Format"] == "Value":
			line_info[field_name] = int(field_content)
		if field["Format"] == "Count":
			line_info[field_name] = int(field_content)
		if field["Format"] == "Julian Date":
			line_info[field_name] = datetime.datetime.strptime(field_content[0:5], '%y%j').strftime('%Y/%m/%d')
		if field["Format"] == "DDMMYY Date":
			line_info[field_name] = datetime.datetime.strptime(field_content, '%d%m%y').strftime('%Y/%m/%d')
		if field["Format"] == "YYMMDD Date":
			line_info[field_name] = datetime.datetime.strptime(field_content, '%y%m%d').strftime('%Y/%m/%d')
		if field["Format"] == "HHMMSS Time":
			line_info[field_name] = datetime.datetime.strptime(field_content, '%H%M%S').strftime('%H:%M:%S')
		if field["Format"] == "White Space":
			line_info[field_name] = field_content.strip()
		if field["Format"] == "Look Up" :
			line_info[field_name] = field["Description"][field_content]
	return line_info
		

def process_file_header(header_line):
	file_header_info = process_line(header_line, header_line_spec)
	file_creation_date = file_header_info["File Creation Date"]
	#print file_creation_date
	# pprint.pprint(file_header_info)

def process_company_header(company_line):
	company_header_info = process_line(company_line, company_line_spec)
	return company_header_info["Company ID"]
	
def process_outlet_header(outlet_line):
	outlet_header_info = process_line(outlet_line, outlet_line_spec)
	return outlet_header_info["Merchant ID"]

def process_transaction_line(transaction_data_line, supplement_data_line, current_company_id, current_merchant_id):
	transaction_info = process_line(transaction_data_line, transaction_data_line_spec)
	supplement_transaction_info = process_line(supplement_data_line, supplement_data_line_spec)
	transaction_info_total = transaction_info.copy()
	transaction_info_total.update(supplement_transaction_info)
	transaction_info_total["Company ID"] = current_company_id
	transaction_info_total["Merchant ID"] = current_merchant_id
	if transaction_info_total["Transaction Type"] == "Purchase":
		transaction_info_total["Transaction Amount"] = float(transaction_info_total["Transaction Value"])/(10**transaction_info_total["Transaction Exponent"])
	if transaction_info_total["Transaction Type"] == "Refund":
		transaction_info_total["Transaction Amount"] = float(transaction_info_total["Transaction Value"])/(10**transaction_info_total["Transaction Exponent"]) * (-1)
	if transaction_info_total["Transaction Type"] == "Purchase":
		transaction_info_total["Settlement Amount"] = float(transaction_info_total["Settlement Value"])/(10**transaction_info_total["Settlement Exponent"])
	if transaction_info_total["Transaction Type"] == "Refund":
		transaction_info_total["Settlement Amount"] = float(transaction_info_total["Settlement Value"])/(10**transaction_info_total["Settlement Exponent"]) * (-1)
	#pprint.pprint(transaction_info_total)
	return transaction_info_total
	

def read(filename):

	transaction_data = []
	with open(filename, 'r') as recon_file:
		for line in recon_file:

			# file header record line
			# TODO: Split the file if there is multiple 00
			if line.startswith('00'):
				process_file_header(line)

			# company header record line
			if line.startswith('05'):
				current_company_id = process_company_header(line)
				
			# outline header record line
			if line.startswith('10'):
				current_merchant_id = process_outlet_header(line)
            
            # transaction data			
			if line.startswith('15'):
			    supplement_transaction_line = next(recon_file)
			    if supplement_transaction_line != '' and supplement_transaction_line.startswith('16'):
					transaction_data.append(process_transaction_line(line, supplement_transaction_line, current_company_id, current_merchant_id))

	return transaction_data

def output_csv(transaction_data, filename):
	filename += ".csv"
	with open(filename, 'wb') as csv_file:
		csv_writer = csv.writer(csv_file, delimiter = ',')
		header = ["Company ID", "Merchant ID", "Order Code", "Transaction Date", "Transaction Time", "Transaction Type", "Status",
			"Transaction Amount", "Transaction Currency Code", "Settlement Amount", "Settlement Currency Code", "Card Number", 
			"Expiry Date", "Card Type", "Transaction Source", "Airline Ticket Number"]
		csv_writer.writerow (header)
		for transcation in transaction_data:
			csv_writer.writerow([transcation[column_name] for column_name in header])


if __name__ == '__main__':
	
	filename = str(sys.argv[1])

	if filename.startswith("MA.PISCESSW.#M.RECON"):
		# Supply source recon file
		transaction_data = read(filename)

		# Consolidate into the CSV
		output_csv(transaction_data, filename)
	else:
		try:
			raise ValueError("Input File is not a RECON file from MFG server")
		except ValueError:
			print "Error"
			print "Input File is not a valid RECON file from MFG server"
