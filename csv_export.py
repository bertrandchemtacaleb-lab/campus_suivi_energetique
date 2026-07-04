"""Export CSV générique à partir d'une liste de dictionnaires ou d'un DataFrame."""
import pandas as pd
from datetime import datetime
import os


def generate_csv_export(records: list[dict], output_dir: str = "/tmp", name: str = "export") -> str:
    filename = f"{name}_{datetime.now():%Y%m%d_%H%M%S}.csv"
    path = os.path.join(output_dir, filename)
    pd.DataFrame(records).to_csv(path, index=False, encoding="utf-8")
    return path
