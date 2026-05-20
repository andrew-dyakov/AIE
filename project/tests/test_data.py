from src.config import load_yaml

def test_config_loads():
    cfg = load_yaml("data.yaml")
    assert "source_path" in cfg
    assert "columns" in cfg

def test_data_paths_exist():
    from src.config import DATA_DIR
    assert DATA_DIR.exists(), f"Папка data не найдена: {DATA_DIR}"
    assert list(DATA_DIR.glob("*.csv")), "CSV файлы в data/ отсутствуют"