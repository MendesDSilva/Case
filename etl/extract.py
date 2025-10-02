import pandas as pd
from config import RAW_PATH

def extract_excel():
    return pd.read_excel(RAW_PATH, sheet_name="Planilha1")
