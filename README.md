# EMIS-Implementation
Worldpay Streamline Reconcilation Files Implementation

## How to use
- Obtain the Transaction Reconcilation File from the MFG Server, File name on server: `\Outgoing\MA.PISCESSW.#M.RECON.nnnn.Dddmmyy`
- Type `python EMIS_Process.py [MA.PISCESSW.#M.RECON.nnnn.Dddmmyy]` on Command Line Interface

## Input and Output
- Input: Please make sure the file name entered is valid, Error message will be shown if file name is invalid
- Output: Output CSV file with fields: "Company ID", "Merchant ID", "Order Code", "Transaction Date", "Transaction Time", "Transaction Type", "Status", 
    "Transaction Amount", "Transaction Currency Code", "Settlement Amount", "Settlement Currency Code", "Card Number", 
		"Expiry Date", "Card Type", "Transaction Source", "Airline Ticket Number"
		
## Requirement:
Python 2.7 installed
