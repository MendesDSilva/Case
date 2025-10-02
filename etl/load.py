from config import READY_DIR
from datetime import datetime

def load_to_excel(df):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_path = READY_DIR / f"Case_Assistente_Comercial_PowerBI.xlsx"
    df.to_excel(file_path, index=False)
    print(f"✅ Arquivo salvo em: {file_path}")
