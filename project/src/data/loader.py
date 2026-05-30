import pandas as pd
from pathlib import Path
from sklearn.model_selection import train_test_split
from ..config import load_yaml, DATA_DIR


def load_and_prepare_data():
    data_cfg = load_yaml("data.yaml")
    exp_cfg = load_yaml("experiment.yaml")

    filename = Path(data_cfg["source_path"]).name
    data_path = DATA_DIR / filename

    if not data_path.exists():
        raise FileNotFoundError(f"Dataset not found at: {data_path}")

    df = pd.read_csv(data_path, sep=data_cfg["separator"], decimal=data_cfg["decimal"])
    df = df.dropna(how=data_cfg["dropna_how"]).reset_index(drop=True)

    num_cols = data_cfg["columns"]["numeric"]
    cat_cols = data_cfg["columns"]["categorical"]
    target_cols = data_cfg["columns"]["targets"]

    df[cat_cols] = df[cat_cols].astype("category")

    X = df.drop(columns=target_cols)
    y = df[target_cols]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=exp_cfg["test_size"], random_state=exp_cfg["random_state"]
    )
    return X_train, X_test, y_train, y_test, num_cols, cat_cols, target_cols
