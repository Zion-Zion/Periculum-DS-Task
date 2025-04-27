from periculum_functions import get_data_from_pdf, extract_data
import json
import tabula # For parsing PDF files
import datetime
import re
import os # To fix the path issue on my PC

# Get the current directory of this python script file
current_dir = os.path.dirname(os.path.abspath(__file__))
pdf_file_path = os.path.join(current_dir, 'home_inventory.pdf') # Path to the PDF file tht is in the same folder as this script
json_file_path = os.path.join(current_dir, 'output.json') # Path to save the output JSON file in the sam folder as the remaming files


# 1: Get raw text from PDF
raw_text = get_data_from_pdf(pdf_file_path)

# 2: Extract structured data
final_dict = extract_data(raw_text)

# 3: Save extracted data to JSON file
with open(json_file_path, 'w') as f:
    json.dump(final_dict, f, indent=4)