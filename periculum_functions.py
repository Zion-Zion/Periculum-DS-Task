import tabula

def get_data_from_pdf(pdf_path):
    """
    Reads a PDF from the specified path and returns the raw text data as a list.
    """
    # Reading the PDF into dataframes (one per page)
    df_ = tabula.read_pdf(pdf_path, stream=False, pages="all", guess=False)
    return df_


import re
from datetime import datetime


class OwnerInfo:
    def __init__(self, name, address, city_zip, telephone):
        self.name = name
        self.address = address
        self.city_zip = city_zip
        self.telephone = telephone

class Inventory:
    def __init__(self, item_number, area, description, source, purchase_date, style, serial_number, value, condition):
        self.item_number = item_number
        self.area = area
        self.description = description
        self.source = source
        self.purchase_date = purchase_date
        self.style = style
        self.serial_number = serial_number
        self.value = value
        self.condition = condition

def extract_data(df_):
    """
    Extracts and processes the OwnerInfo and Inventory data from the aligned dataframe.
    Returns a dictionary with OwnerInfo as first-level keys and Inventory as second-level keys.
    """
    # Extract Owner Info
    owner_name = df_[0].iloc[1, 1]
    owner_address = df_[0].iloc[2, 1]
    owner_city_zip = df_[0].iloc[3, 1]
    owner_telephone = df_[0].iloc[4, 1]
    full_address = f"{owner_address}, {owner_city_zip}"

    owner_info = OwnerInfo(owner_name, full_address, owner_city_zip, owner_telephone)

    # Initialize lists for inventory details
    Item_Number = []
    Area = []
    Item_Description = []
    Source = []
    Purchase_Date = []
    Style = []
    Serial_Number = []
    Value = []
    Condition = []

    # Items Numbers
    # For the first page having Owner Info table
    # Start from the 7th row (index 6) to skip the header and owner info
    for i in df_[0].iloc[6:].iterrows():
        information = df_[0].iloc[i[0]][0]
        match = re.search(r'\d+', str(information))
        if match:
            Item_Number.append(match.group())


    for i in range(1, len(df_)):
        # Get the header row
        header_row = df_[i].iloc[0].index
        header_info = header_row[0]
        match = re.search(r'\d+', str(header_info))
        if match:
            Item_Number.append(match.group())
        
        # Get the rest of the rows
        for j in df_[i].iloc[0:].iterrows():
            row_info = df_[i].iloc[j[0]][0]
            match = re.search(r'\d+', str(row_info))
            if match:
                Item_Number.append(match.group())


    # The remaining code follow the same syntax to extract frmo the firt page first before other pages of the document


    # Areas
    for i in df_[0].iloc[6:].iterrows():
        information = i[1][0]
        match = re.search(r'[A-Z][a-z]+.+', str(information))
        if match:
            Area.append(match.group())


    for i in range(1, len(df_)):
        if len(df_[i].columns) > 5:
            header_row = df_[i].columns

            # collect first column
            header_info = header_row[0]
            match = re.search(r'[A-Z][a-z]+.+', str(header_info))
            if match:
                Area.append(match.group())

            # If second column exists, extract it too
            if len(header_row) > 1:
                header_info = header_row[1]
                match = re.search(r'[A-Z][a-z]+.+', str(header_info))
                if match:
                    Area.append(match.group())


            # Loop through rows
            for j in df_[i].iloc[0:].iterrows():
                row_info = j[1][0]
                match = re.search(r'[A-Z][a-z]+.+', str(row_info))
                if match:
                    Area.append(match.group())

                if df_[i].shape[1] > 1:
                    row_info = j[1][1]
                    match = re.search(r'[A-Z][a-z]+.+', str(row_info))
                    if match:
                        Area.append(match.group())


    # Item Descriptions
    for i in df_[0].iloc[6:].iterrows():
        information = i[1][1]
        match = re.search(r'[A-Za-z][A-Za-z ]+', str(information))
        if match:
            Item_Description.append(match.group())


    for i in range(1, len(df_)):
        if len(df_[i].columns) > 5:
            header_row = df_[i].columns

            if len(header_row) > 1:
                header_info = header_row[2]
                match = re.search(r'[A-Za-z][A-Za-z ]+', str(header_info))
                if match:
                    Item_Description.append(match.group())

            # loop through rows
            for j in df_[i].iloc[0:].iterrows():
            
                if df_[i].shape[1] > 1:
                    row_info = j[1][2]
                    match = re.search(r'[A-Za-z][A-Za-z ]+', str(row_info))
                    if match:
                        Item_Description.append(match.group())


    # Source
    for i in df_[0].iloc[6:].iterrows():
        information = i[1][2]
        match = re.search(r'[A-Za-z ]+[A-Za-z]+', str(information))
        if match:
            Source.append(match.group())

    for i in range(1, len(df_)):
        if len(df_[i].columns) > 5:
            header_row = df_[i].columns

            if len(header_row) > 1:
                header_info = header_row[3]
                match = re.search(r'[A-Za-z][A-Za-z ]+', str(header_info))
                if match:
                    Source.append(match.group())

            # loop through rows
            for j in df_[i].iloc[0:].iterrows():
                
                if df_[i].shape[1] > 1:
                    row_info = j[1][3]
                    match = re.search(r'[A-Za-z][A-Za-z ]+', str(row_info))
                    if match:
                        Source.append(match.group())


    # Purchase Date
    for i in df_[0].iloc[6:].iterrows():
        information = i[1][2]
        match = re.search(r'\d{2}/\d{2}/\d{4}', str(information))
        if match:
            Purchase_Date.append(match.group())


    for i in range(1, len(df_)):
        if len(df_[i].columns) > 5:
            header_row = df_[i].columns

            if len(header_row) > 1:
                header_info = header_row[4]
                match = re.search(r'\d{2}/\d{2}/\d{4}', str(header_info))
                if match:
                    Purchase_Date.append(match.group())

            # loop through rows
            for j in df_[i].iloc[0:].iterrows():
            
                if df_[i].shape[1] > 1:
                    row_info = j[1][4]
                    match = re.search(r'\d{2}/\d{2}/\d{4}', str(row_info))
                    if match:
                        Purchase_Date.append(match.group())



    # Style
    for i in df_[0].iloc[6:].iterrows():
        information = i[1][2]
        match = re.search(r'\d{2}/\d{2}/\d{4}', str(information))
        if match:
            Style.append(information[match.end():].strip())



    for i in range(1, len(df_)):
        if len(df_[i].columns) > 5:
            header_row = df_[i].columns

            if len(header_row) > 1:
                header_info = header_row[5]
                match = re.search(r'[A-Za-z][A-Za-z ]+', str(header_info))
                if match:
                    Style.append(match.group())

            # loop through rows
            for j in df_[i].iloc[0:].iterrows():

                if df_[i].shape[1] > 1:
                    row_info = j[1][5]
                    match = re.search(r'[A-Za-z][A-Za-z ]+', str(row_info))
                    if match:
                        Style.append(match.group())


    # Serial Number
    for i in df_[0].iloc[6:].iterrows():
        information = i[1][4]
        match = re.search(r'\S+', str(information))
        if match:
            Serial_Number.append(match.group())


    for i in range(1, len(df_)):
        if len(df_[i].columns) > 5:
            header_row = df_[i].columns

            if len(header_row) > 1:
                header_info = header_row[6]
                match = re.search(r'\S+', str(header_info))
                if match:
                    Serial_Number.append(match.group())

            # loop through rows
            for j in df_[i].iloc[0:].iterrows():
                
                if df_[i].shape[1] > 1:
                    row_info = j[1][6]
                    match = re.search(r'\S+', str(row_info))
                    if match:
                        Serial_Number.append(match.group())


    # Value
    for i in df_[0].iloc[6:].iterrows():
        information = i[1][6]
        match = re.search(r'\d{1,3}(?:,\d{3})*(?:\.\d+)?', str(information))
        if match:
            Value.append(match.group())



    for i in range(1, len(df_)):
        if len(df_[i].columns) > 5:
            header_row = df_[i].columns

            if len(header_row) > 1:
                header_info = header_row[8]
                match = re.search(r'\d{1,3}(?:,\d{3})*(?:\.\d+)?', str(header_info))
                if match:
                    Value.append(match.group())

            # loop through rows
            for j in df_[i].iloc[0:].iterrows():

                if df_[i].shape[1] > 1:
                    row_info = j[1][8]
                    match = re.search(r'\d{1,3}(?:,\d{3})*(?:\.\d+)?', str(row_info))
                    if match:
                        Value.append(match.group())


    # Condition
    for i in range(1, len(df_)):
        if len(df_[i].columns) < 5:
            for row in df_[i].iloc[1:, 1]:
                match = re.search(r'[A-Za-z ]+', str(row))
                if match:
                    Condition.append(match.group())
            break

    for i in range(1, len(df_)):
        if len(df_[i].columns) == 1:
            # Grab the header
            header = df_[i].columns[0]
            match = re.search(r'[A-Za-z ]+', str(header))
            if match:
                Condition.append(match.group())
            
            # Grab all the rows under it
            for row in df_[i].iloc[:, 0]:
                match = re.search(r'[A-Za-z ]+', str(row))
                if match:
                    Condition.append(match.group())


    
    # Assemble all the data into a final dictionary
    inventory_data = []
    source_style_area = []

    for i in range(len(Item_Number)):
        raw_date = Purchase_Date[i]
        try:
            # Convert date to ISO format
            parsed_date = datetime.strptime(raw_date, "%d/%m/%Y")
            purchase_date_iso = parsed_date.isoformat()
        except:
            purchase_date_iso = None
    
        # Combine Source, Style, and Area into one string
        combined_source_style_area = f"{Source[i]} {Style[i]} {Area[i]}"
        
        # Append the inventory data to the list
        inventory_data.append({
            "item_number": Item_Number[i],
            "description": Item_Description[i],
            "source_style_area": combined_source_style_area,
            "purchase_date": purchase_date_iso,
            "serial_number": Serial_Number[i],
            "value": Value[i],
            "condition": Condition[i]
        })
   
    # Return a dictionary with required structure
    return {
        "owner_info": {
            "name": owner_info.name,
            "address": owner_info.address,
            "city_zip": owner_info.city_zip,
            "telephone": owner_info.telephone
        },
        "data": inventory_data
    }




