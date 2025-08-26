import pandas as pd
from typing import Iterator, Dict
from .config import CSV_FILE, BATCH_SIZE


def read_csv_in_batches(file_path: str = CSV_FILE, batch_size: int = BATCH_SIZE) -> Iterator[pd.DataFrame]:
  
    for chunk in pd.read_csv(file_path, chunksize=batch_size):
        yield chunk


def df_to_dict_list(df: pd.DataFrame) -> list[Dict]:

    return df.to_dict(orient="records")
