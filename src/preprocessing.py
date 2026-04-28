import pandas as pd

def load_data(path):
    return pd.read_excel(path)

def preprocess(df):
    df = df.copy()

    df = df.dropna(subset=["transfusion"])

    return df
