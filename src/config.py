# src/config.py

from pathlib import Path

# Reproducibility
RANDOM_STATE = 42

# Paths
PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"

# Dataset
DATASET_NAME = "bank-additional-full"

# Target
TARGET_COL = "y"
POSITIVE_CLASS = "yes"

# Columns to exclude (Data Leakage / not available before contact)
DROP_COLS = [
    "duration"
]

# Train/Test Split
TEST_SIZE = 0.2  # nur relevant bei Random Split
