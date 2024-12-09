import os

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