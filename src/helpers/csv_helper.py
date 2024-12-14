import pandas as pd
import csv

def is_csv_empty(path):
    df = pd.read_csv(path, sep=',', on_bad_lines='skip')

    if df.empty:
        return True
    else:
        return False