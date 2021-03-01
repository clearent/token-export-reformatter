# Overview
Merchants or integrators will occasionally request an export of the token data stored within Clearent's vault.  This is typically done when migrating to another provider.
The current version of Clearent's token exporter will produce a fixed-width file containing the following fields:

- Data record indicator ("data:")
- Card number
- Expiration date
- Clearent token ID
- Address
- Postal code
- First name
- Last name
- Description/Legacy token ID

While some like the default fixed-width format, others prefer the data in a CSV file with labeled columns.

Token export files are encrypted with the recipient's PGP key at the time of generation so that no one other than the recipient can view the data.  Therefore, Clearent staff
cannot open the files to manipulate them.  However, this small script can be run to convert the fixed-width file into CSV format.

# Usage
Execute the script using python:  `python create_csv.py`

You will be prompted for the path to the existing (decrypted) file.  (e.g. `/Users/jdoe/00000123456_clearent_export.gpg`)

You will also be prompted for the desired path of the output file.  (e.g. `/Users/jdoe/export.csv`)

The result will be a comma-delimited file with a row of headers to denote each piece of data.

