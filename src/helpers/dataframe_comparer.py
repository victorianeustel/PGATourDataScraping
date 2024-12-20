import pandas as pd

def are_df_column_count_equal(df1: pd.DataFrame, df2: pd.DataFrame):
    df_count1 = len(df1.columns)
    df_count2 = len(df2.columns)
    return df_count1 == df_count2