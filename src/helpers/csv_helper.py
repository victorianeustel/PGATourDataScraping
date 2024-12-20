import pandas as pd
import csv

def is_csv_empty(path):
    df = pd.read_csv(path, sep=',', on_bad_lines='skip')
    return df.empty

def read_csv(directory_path:str, file_name: str, new_line:str = ''):
    file_path = '/'.join(directory_path, file_name)
    with open(file_path, newline=new_line) as f:
        reader = csv.reader(f)
        next(reader, None)  # Skip the header.
        for row in reader:
            print(row)
            
def create_or_append_csv(path:str = "", 
    fileName: str = None, 
    fileWritingType: str = "w", 
    header: list = None, 
    content_rows: list = None):
    
    if (fileName == None): filePath = path
    else: filePath = '/'.join([path, fileName])
    with open(filePath, fileWritingType, newline='\n') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_ALL)
        if (header is not None):
            writer.writerow(header)
        if (content_rows is not None):
            for row in content_rows:
                writer.writerow(row)
