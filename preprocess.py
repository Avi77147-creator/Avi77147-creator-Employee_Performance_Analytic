
import pandas as pd

def load_data(filepath):
    return pd.read_csv(filepath)

def clean_data(df):
    df = df.dropna()
    df['Department'] = df['Department'].str.strip().str.title()
    return df
