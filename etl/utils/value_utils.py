import pandas as pd

def limpar_valor(valor):
    if pd.isna(valor):
        return None
    s = str(valor).strip()
    s = s.replace("R$", "").replace("%", "").replace(".", "").replace(",", ".")
    try:
        return float(s)
    except:
        return None
