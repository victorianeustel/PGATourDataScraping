import os
import csv

def create_directory(path):
    print(path)
    if (os.path.isdir(path)):
        return
    os.mkdir(path)
    

def create_or_append_csv(path:str, fileName: str, fileWritingType: str = "w", 
            header: list = None, content_rows: list = None):
    filePath = '/'.join([path, fileName])
    with open(filePath, fileWritingType, newline='\n') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_ALL)
        if (header is not None):
            writer.writerow(header)
        if (content_rows is not None):
            for row in content_rows:
                writer.writerow(row)