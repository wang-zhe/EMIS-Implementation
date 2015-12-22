
# Record down the specification from EMIS Tech Spec V19
# Each Field with Name, Start Pos, Length, Format, Description

header_line_spec = [
	{
		"Name" : "Count",
		"Start Pos." : 24,
		"Length": 7,
		"Format": "Count",
		"Description" : "Count of 05 record in file"
	},
	{
		"Name" : "Accepted Debits",
		"Start Pos." : 31,
		"Length": 11,
		"Format": "Value",
		"Description" : "Value (Hash) of accepted refunds (in minor units)"
	},
	{
		"Name" : "Rejected Debits",
		"Start Pos." : 42,
		"Length": 11,
		"Format": "Value",
		"Description" : "Value (Hash) of rejected refunds (in minor units)"
	},
	{
		"Name" : "Pending Debits",
		"Start Pos." : 53,
		"Length": 11,
		"Format": "Value",
		"Description" : "Value (Hash) of pending refunds (in minor units)"
	},
	{
		"Name" : "Accepted Credits",
		"Start Pos." : 64,
		"Length": 11,
		"Format": "Value",
		"Description" : "Value (Hash) of accepted sales (in minor units)"
	},
	{
		"Name" : "Rejected Credits",
		"Start Pos." : 75,
		"Length": 11,
		"Format": "Value",
		"Description" : "Value (Hash) of rejected sales (in minor units)"
	},
	{
		"Name" : "Pending Credits",
		"Start Pos." : 86,
		"Length": 11,
		"Format": "Value",
		"Description" : "Value (Hash) of pending sales (in minor units)"
	},
	{
		"Name" : "Accepted Debits Count",
		"Start Pos." : 97,
		"Length": 7,
		"Format": "Value",
		"Description" : "Count of accepted refunds"
	},
	{
		"Name" : "Rejected Debits Count",
		"Start Pos." : 104,
		"Length": 7,
		"Format": "Value",
		"Description" : "Count of rejected refunds"
	},
	{
		"Name" : "Pending Debits Count",
		"Start Pos." : 111,
		"Length": 7,
		"Format": "Value",
		"Description" : "Count of pending refunds"
	},
	{
		"Name" : "Accepted Credits Count",
		"Start Pos." : 118,
		"Length": 7,
		"Format": "Value",
		"Description" : "Count of accepted sales"
	},
	{
		"Name" : "Rejected Credits Count",
		"Start Pos." : 125,
		"Length": 7,
		"Format": "Value",
		"Description" : "Count of rejected sales"
	},
	{
		"Name" : "Pending Credits Count",
		"Start Pos." : 132,
		"Length": 7,
		"Format": "Value",
		"Description" : "Count of pending sales"
	},
	{
		"Name" : "File Creation Date",
		"Start Pos." : 139,
		"Length": 6,
		"Format": "Julian Date",
		"Description" : "File Creation Date"
	}
]

company_line_spec = [
	{
		"Name" : "Company ID",
		"Start Pos." : 11,
		"Length": 13,
		"Format": "Value",
		"Description" : "Company ID"
	},
	{
		"Name" : "Count",
		"Start Pos." : 24,
		"Length": 7,
		"Format": "Count",
		"Description" : "Count of 10 record in file"
	},
	{
		"Name" : "Accepted Debits",
		"Start Pos." : 31,
		"Length": 11,
		"Format": "Value",
		"Description" : "Value (Hash) of accepted refunds (in minor units)"
	},
	{
		"Name" : "Rejected Debits",
		"Start Pos." : 42,
		"Length": 11,
		"Format": "Value",
		"Description" : "Value (Hash) of rejected refunds (in minor units)"
	},
	{
		"Name" : "Pending Debits",
		"Start Pos." : 53,
		"Length": 11,
		"Format": "Value",
		"Description" : "Value (Hash) of pending refunds (in minor units)"
	},
	{
		"Name" : "Accepted Credits",
		"Start Pos." : 64,
		"Length": 11,
		"Format": "Value",
		"Description" : "Value (Hash) of accepted sales (in minor units)"
	},
	{
		"Name" : "Rejected Credits",
		"Start Pos." : 75,
		"Length": 11,
		"Format": "Value",
		"Description" : "Value (Hash) of rejected sales (in minor units)"
	},
	{
		"Name" : "Pending Credits",
		"Start Pos." : 86,
		"Length": 11,
		"Format": "Value",
		"Description" : "Value (Hash) of pending sales (in minor units)"
	},
	{
		"Name" : "Accepted Debits Count",
		"Start Pos." : 97,
		"Length": 7,
		"Format": "Value",
		"Description" : "Count of accepted refunds"
	},
	{
		"Name" : "Rejected Debits Count",
		"Start Pos." : 104,
		"Length": 7,
		"Format": "Value",
		"Description" : "Count of rejected refunds"
	},
	{
		"Name" : "Pending Debits Count",
		"Start Pos." : 111,
		"Length": 7,
		"Format": "Value",
		"Description" : "Count of pending refunds"
	},
	{
		"Name" : "Accepted Credits Count",
		"Start Pos." : 118,
		"Length": 7,
		"Format": "Value",
		"Description" : "Count of accepted sales"
	},
	{
		"Name" : "Rejected Credits Count",
		"Start Pos." : 125,
		"Length": 7,
		"Format": "Value",
		"Description" : "Count of rejected sales"
	},
	{
		"Name" : "Pending Credits Count",
		"Start Pos." : 132,
		"Length": 7,
		"Format": "Value",
		"Description" : "Count of pending sales"
	}
]

outlet_line_spec = [
	{
		"Name" : "Merchant ID",
		"Start Pos." : 11,
		"Length": 13,
		"Format": "Value",
		"Description" : "Merchant ID"
	},
	{
		"Name" : "Trading Day",
		"Start Pos." : 24,
		"Length": 6,
		"Format": "DDMMYY Date",
		"Description" : "Trading Date"
	},
	{
		"Name" : "Processing Date",
		"Start Pos." : 30,
		"Length": 6,
		"Format": "YYMMDD Date",
		"Description" : "Processing Date"
	},
	{
		"Name" : "Accepted Debits",
		"Start Pos." : 36,
		"Length": 11,
		"Format": "Value",
		"Description" : "Value (Hash) of accepted refunds (in minor units)"
	},
	{
		"Name" : "Rejected Debits",
		"Start Pos." : 47,
		"Length": 11,
		"Format": "Value",
		"Description" : "Value (Hash) of rejected refunds (in minor units)"
	},
	{
		"Name" : "Pending Debits",
		"Start Pos." : 58,
		"Length": 11,
		"Format": "Value",
		"Description" : "Value (Hash) of pending refunds (in minor units)"
	},
	{
		"Name" : "Accepted Credits",
		"Start Pos." : 69,
		"Length": 11,
		"Format": "Value",
		"Description" : "Value (Hash) of accepted sales (in minor units)"
	},
	{
		"Name" : "Rejected Credits",
		"Start Pos." : 80,
		"Length": 11,
		"Format": "Value",
		"Description" : "Value (Hash) of rejected sales (in minor units)"
	},
	{
		"Name" : "Pending Credits",
		"Start Pos." : 91,
		"Length": 11,
		"Format": "Value",
		"Description" : "Value (Hash) of pending sales (in minor units)"
	},
	{
		"Name" : "Accepted Debits Count",
		"Start Pos." : 102,
		"Length": 7,
		"Format": "Value",
		"Description" : "Count of accepted refunds"
	},
	{
		"Name" : "Rejected Debits Count",
		"Start Pos." : 109,
		"Length": 7,
		"Format": "Value",
		"Description" : "Count of rejected refunds"
	},
	{
		"Name" : "Pending Debits Count",
		"Start Pos." : 116,
		"Length": 7,
		"Format": "Value",
		"Description" : "Count of pending refunds"
	},
	{
		"Name" : "Accepted Credits Count",
		"Start Pos." : 123,
		"Length": 7,
		"Format": "Value",
		"Description" : "Count of accepted sales"
	},
	{
		"Name" : "Rejected Credits Count",
		"Start Pos." : 130,
		"Length": 7,
		"Format": "Value",
		"Description" : "Count of rejected sales"
	},
	{
		"Name" : "Pending Credits Count",
		"Start Pos." : 137,
		"Length": 7,
		"Format": "Value",
		"Description" : "Count of pending sales"
	}
]

transaction_data_line_spec = [
	{
		"Name" : "Card Number",
		"Start Pos." : 11,
		"Length": 19,
		"Format": "White Space",
		"Description" : "Obfuscated Card No."
	},
	{
		"Name" : "Expiry Date",
		"Start Pos." : 30,
		"Length": 4,
		"Format": "Default",
		"Description" : "Expiry Date"
	},
	{
		"Name" : "Transaction Value (GBP)",
		"Start Pos." : 34,
		"Length": 11,
		"Format": "Value",
		"Description" : "Value in GBP (in minor units)"
	},
	{
		"Name" : "Transaction Date",
		"Start Pos." : 45,
		"Length": 6,
		"Format": "DDMMYY Date",
		"Description" : "Date of transaction DDMMYY"
	},
	{
		"Name" : "Transaction Time",
		"Start Pos." : 51,
		"Length": 6,
		"Format": "HHMMSS Time",
		"Description" : "Time of transaction DDMMYY"
	},
	{
		"Name" : "Transaction Type",
		"Start Pos." : 57,
		"Length": 1,
		"Format": "Look Up",
		"Description" : {
			"0" : "Purchase",
			"5" : "Refund",
			"3" : "Purchase with cash back",
			"2" : "Cash advance"
		}
	},
	{
		"Name" : "Transaction Source",
		"Start Pos." : 58,
		"Length": 1,
		"Format": "Look Up",
		"Description" : {
			"0" : "Offline key entry",
			"1" : "Mail order - telephone",
			"2" : "ICC and online PIN (RFU)",
			"3" : "ICC and offline PIN (or offline PIN & Signature)",
			"4" : "Signed voucher - magnetic stripe captured",
			"5" : "Signed voucher keyed at POS",
			"6" : "Unattended device without PIN",
			"7" : "Pin verified transaction recovered after sale",
			"8" : "Terminal recovery keyed by acceptor",
			"9" : "Terminal recovery keyed by acquirer",
			"A" : "ICC and signature (or no cardholder verification)",
			"B" : "ICC fallback transaction to magnetic stripe",
			"C" : "Secure transaction with cardholder certificate",
			"D" : "Non Authenticated Security transaction with 3D Secure/ SPA UCAF merchant certificate",
			"E" : "Non authenticated transaction with no 3D Secure/ SPA UCAF merchant certificate eg SSL protocol",
			"F" : "E-commerce static cardholder authentication",
			"M" : "qVSDC or M/Chip contactless transactions",
			"N" : "MSD Contactless transactions"
		}
	},
	{
		"Name" : "Status",
		"Start Pos." : 65,
		"Length": 1,
		"Format": "Look Up",
		"Description" : {
			"A" : "Accepted",
			"P" : "Pending",
			"R" : "Rejected",
		}
	},
	{
		"Name" : "Transaction Value",
		"Start Pos." : 68,
		"Length": 9,
		"Format": "Value",
		"Description" : "Local Value(in minor units)"
	},
	{
		"Name" : "Transaction Currency Code",
		"Start Pos." : 77,
		"Length": 3,
		"Format": "Default",
		"Description" : "Local Currency Code (ISO alpha)"
	},
	{
		"Name" : "Transaction Exponent",
		"Start Pos." : 80,
		"Length": 1,
		"Format": "Value",
		"Description" : "Local Exponent"
	},
	{
		"Name" : "Settlement Value",
		"Start Pos." : 81,
		"Length": 9,
		"Format": "Value",
		"Description" : "Local Value(in minor units)"
	},
	{
		"Name" : "Settlement Currency Code",
		"Start Pos." : 90,
		"Length": 3,
		"Format": "Default",
		"Description" : "Local Currency Code (ISO alpha)"
	},
	{
		"Name" : "Settlement Exponent",
		"Start Pos." : 93,
		"Length": 1,
		"Format": "Value",
		"Description" : "Local Exponent"
	},
	{
		"Name" : "Acquired / Processed indicator",
		"Start Pos." : 94,
		"Length": 1,
		"Format": "Look Up",
		"Description" : {
			"A" : "Acquired",
			"P" : "Processed"
		}
	},
	{
		"Name" : "Card Type",
		"Start Pos." : 95,
		"Length": 5,
		"Format": "Look Up",
		"Description" : {
			"VP002" : "MasterCard Commercial",
			"VPMCB" : "MasterCard Business",
			"VPMCO" : "MasterCard Corporate",
			"AC000" : "MasterCard Credit",
			"VPMCF" : "MasterCard Fleet",
			"VPMCP" : "MasterCard Purchase",
			"ACMCW" : "MasterCard Signia",
			"ACMNW" : "MasterCard World",
			"VP001" : "Visa Commercial",
			"VPVIB" : "Visa Business",
			"VPVID" : "Visa Commerce",
			"VPVIR" : "Visa Corporate",
			"BC000" : "Visa Credit",
			"VPVIS" : "Visa Purchasing",
			"DM000" : "Debit MasterCard EEA",
			"ACMCY" : "MasterCard Debit Personal International",
			"VPMCX" : "MasterCard Debit Commercial International",
			"DE000" : "Visa Debit",
			"VPVIX" : "Visa Debit Commercial International",
			"BCVIY" : "Visa Debit/Visa Electron Personal International",
			"PE000" : "Visa Electron",
			"PMDOM" : "Maestro (Domestic)",
			"PM001" : "Maestro International"
		}
	}
	
]

supplement_data_line_spec = [
	{
		"Name" : "Auth Code",
		"Start Pos." : 11,
		"Length": 6,
		"Format": "Default",
		"Description" : "Auth code"
	},
	{
		"Name" : "Auth Method",
		"Start Pos." : 17,
		"Length": 1,
		"Format": "Look Up",
		"Description" : {
			"0" : "Authorised by the terminal (transaction within Floor Limit) or not obtained",
			"1" : "Authorised Online to Streamline",
			"2" : "Authorised by voice call to Streamline",
			"9" : "Unknown"
		}
	},
	{
		"Name" : "Card Issue Number",
		"Start Pos." : 18,
		"Length": 2,
		"Format": "Default",
		"Description" : "Card Issue Number"
	},
	{
		"Name" : "Card Start Date",
		"Start Pos." : 20,
		"Length": 4,
		"Format": "Default",
		"Description" : "Card Start Date"
	},
	{
		"Name" : "Cash amount",
		"Start Pos." : 24,
		"Length": 7,
		"Format": "Value",
		"Description" : "Cash amount (in minor unit)"
	},
	{
		"Name" : "Order Code",
		"Start Pos." : 31,
		"Length": 20,
		"Format": "White Space",
		"Description" : "Originators Transaction References"
	},
	{
		"Name" : "Airline Ticket Number",
		"Start Pos." : 51,
		"Length": 14,
		"Format": "White Space",
		"Description" : "Air Ticket Number"
	}
]

