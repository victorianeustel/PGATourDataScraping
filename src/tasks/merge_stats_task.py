from helpers.file_helper import *

def get_groups_of_files():
    files = get_all_files_in_directory('data/stats')
    file_names = [get_path_from_file_path(f) for f in files]
    distinct_file_names = list(set(file_names))
    distinct_file_names.sort()
    return distinct_file_names

def get_year_from_path(file_name: str):
    return file_name.split('/')[2]

def get_df_from_file(file_path: str):
    file_year = get_year_from_path(file_path)
    df = pd.read_csv(file_path, sep=',', on_bad_lines='skip')
    df_rows = len(df)
    year_col = [file_year] * df_rows
    df['YEAR'] = year_col
    first_column = df.pop('YEAR') 
    df.insert(0, 'YEAR', first_column) 

    return df

def run_merge_csv_groups_task():
    file_names = get_groups_of_files()
    for file in file_names:
        file_paths = get_all_files_with_name('data/stats', file)
        df = get_df_from_file(file_paths[0])
        for fp in file_paths[1:len(file_paths)]:
            current_df = get_df_from_file(fp)
            df = df._append(current_df, ignore_index=True)
        df.to_csv('data/combined_stats/' + file, index=False)  