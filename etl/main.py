from extract import extract_excel
from transform import transform
from load import load_to_excel

if __name__ == "__main__":
    df_raw = extract_excel()
    df_ready = transform(df_raw)
    load_to_excel(df_ready)
