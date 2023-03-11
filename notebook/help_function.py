import pandas as pd

def get_unique_values(df):
    unique_values_dict = {}
    for column in df.columns:
        if df[column].dtype == 'object':
            unique_values_dict[column] = set(df[column].unique())
    return unique_values_dict
