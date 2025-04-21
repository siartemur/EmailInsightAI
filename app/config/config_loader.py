import yaml
from pathlib import Path

CONFIG_PATH = Path("app/config/config.yaml")

def load_config():
    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)
