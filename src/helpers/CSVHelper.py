import pandas as pd

def IsCSVEmpty(path):
    df = pd.read_csv(path, sep=',', on_bad_lines='skip')

    if df.empty:
        return True
    else:
        return False