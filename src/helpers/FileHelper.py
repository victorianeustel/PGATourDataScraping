import os
from CSVHelper import IsCSVEmpty

# Create directory 
def CreateDirectory(directory_name):
    try:
        os.mkdir(directory_name)
        print(f"Directory '{directory_name}' created successfully.")
    except FileExistsError:
        print(f"Directory '{directory_name}' already exists.")
    except PermissionError:
        print(f"Permission denied: Unable to create '{directory_name}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

def CleanName(name: str):
    cleaned_name = name \
        .replace('- ', '') \
        .replace(' ', '_') \
        .replace(',', '_') \
        .replace(':', '') \
        .replace('/', '') \
        .replace('*', '') \
        .replace('<', 'less-than') \
        .replace('>', 'greater-than') \
        .replace('|', 'or') \
        .replace('?', '') \
        .replace('\\', '') \
        .lower()

    return cleaned_name

# Delete empty directories starting from child directory up
def DeleteEmptyDirectories(root):

    deleted = set()
    
    for current_dir, subdirs, files in os.walk(root, topdown=False):

        still_has_subdirs = False
        for subdir in subdirs:
            if os.path.join(current_dir, subdir) not in deleted:
                still_has_subdirs = True
                break
    
        if not any(files) and not still_has_subdirs:
            os.rmdir(current_dir)
            deleted.add(current_dir)

    return deleted

# Delete empty CSV Data files
def DeleteEmptyDataFiles(path: str):
    for subdir, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(".csv"):
                fullPath = os.path.join(subdir, file)
                isEmpty = IsCSVEmpty(os.path.join(subdir, file))
                if isEmpty == True:
                    os.remove(fullPath)