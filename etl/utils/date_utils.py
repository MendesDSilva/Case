import re

def converter_data_portugues(data_str):
    meses = {
        "janeiro": "01", "fevereiro": "02", "março": "03", "abril": "04",
        "maio": "05", "junho": "06", "julho": "07", "agosto": "08",
        "setembro": "09", "outubro": "10", "novembro": "11", "dezembro": "12"
    }
    match = re.match(r"(\d{1,2}) de ([a-zç]+) de (\d{4})", str(data_str).lower())
    if match:
        dia, mes_nome, ano = match.groups()
        mes = meses.get(mes_nome)
        return f"{int(dia):02d}/{mes}/{ano}" if mes else None
    return None
