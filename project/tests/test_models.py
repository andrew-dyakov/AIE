import pytest
from pathlib import Path

@pytest.fixture
def artifacts_exist():
    manifest = Path("artifacts/models/best_model_manifest.json")
    if not manifest.exists():
        pytest.skip("Артефакты не найдены. Запустите эксперимент.")

def test_predictor_import(artifacts_exist):
    from src.models.predictor import CoolingPredictor
    assert CoolingPredictor is not None

def test_risk_levels_logic():
    from src.config import load_yaml
    cfg = load_yaml("serving.yaml")
    assert cfg["risk_thresholds"]["low"] < cfg["risk_thresholds"]["medium"]