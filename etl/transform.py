import pandas as pd
import re
from utils.date_utils import converter_data_portugues
from utils.value_utils import limpar_valor

def transform(df):
    df = df.rename(columns={"Unnamed: 0": "Estado", "Unnamed: 1": "Cidade", "Unnamed: 2": "Marca"})
    dates_row = df.iloc[0]
    df_data = df.drop(0).reset_index(drop=True)

    df_long = df_data.melt(id_vars=["Estado", "Cidade", "Marca"], var_name="Metrica", value_name="Valor")
    df_long["Data"] = df_long["Metrica"].map(dates_row).apply(converter_data_portugues)
    df_long["Metrica"] = df_long["Metrica"].str.replace(r"\.\d+$", "", regex=True)
    df_long["Valor"] = df_long["Valor"].apply(limpar_valor)

    return df_long[["Estado", "Cidade", "Marca", "Data", "Metrica", "Valor"]]
