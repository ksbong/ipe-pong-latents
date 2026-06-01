from pathlib import Path
import pandas as pd


def load_metadata(path: str | Path) -> pd.DataFrame:
    path = Path(path)

    if not path.exists():
        raise FileNotFoundError(f"Metadata file not found: {path}")

    if path.suffix == ".csv":
        return pd.read_csv(path)
    if path.suffix in [".pkl", ".pickle"]:
        return pd.read_pickle(path)
    if path.suffix == ".parquet":
        return pd.read_parquet(path)

    raise ValueError(f"Unsupported metadata format: {path.suffix}")