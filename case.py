import pandas as pd
import re
from pathlib import Path
from datetime import datetime

# Caminhos de entrada e saída
RAW_PATH = Path(r"C:\Users\msilva36\OneDrive - ELIS\Documentos\Case\src\raw\Case Assitente Comercial KA.xlsx")
READY_DIR = Path(r"C:\Users\msilva36\OneDrive - ELIS\Documentos\Case\src\ready")

# --- Funções auxiliares ---

# Converte datas no formato "1 de janeiro de 2025" → "01/01/2025"
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
        if mes:
            return f"{int(dia):02d}/{mes}/{ano}"
    return None

# Limpa valores, removendo R$, %, pontos de milhar etc.
def limpar_valor(valor):
    if pd.isna(valor):
        return None
    s = str(valor).strip()
    s = s.replace("R$", "").replace("%", "").replace(".", "").replace(",", ".")
    try:
        return float(s)
    except:
        return None

# --- Função principal ---
def transformar_planilha(raw_file: Path, ready_dir: Path):
    # Carregar planilha
    df = pd.read_excel(raw_file, sheet_name="Planilha1")

    # Renomear colunas fixas
    df = df.rename(columns={"Unnamed: 0": "Estado", "Unnamed: 1": "Cidade", "Unnamed: 2": "Marca"})

    # Linha 0 contém as datas
    dates_row = df.iloc[0]

    # Remover linha de datas
    df_data = df.drop(0).reset_index(drop=True)

    # Transformar em formato longo
    df_long = df_data.melt(id_vars=["Estado", "Cidade", "Marca"], var_name="Metrica", value_name="Valor")

    # Mapear datas
    df_long["Data"] = df_long["Metrica"].map(dates_row)
    df_long["Data"] = df_long["Data"].apply(converter_data_portugues)

    # Limpar métricas
    df_long["Metrica"] = df_long["Metrica"].str.replace(r"\.\d+$", "", regex=True)

    # Limpar valores
    df_long["Valor"] = df_long["Valor"].apply(limpar_valor)

    # Reorganizar colunas
    df_long = df_long[["Estado", "Cidade", "Marca", "Data", "Metrica", "Valor"]]

    # Nome do arquivo com timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    ready_file = ready_dir / f"Case_Assistente_Comercial_PowerBI.xlsx"

    # Exportar
    df_long.to_excel(ready_file, index=False)
    print(f"✅ Arquivo transformado e salvo em: {ready_file}")

# Execução
if __name__ == "__main__":
    transformar_planilha(RAW_PATH, READY_DIR)
