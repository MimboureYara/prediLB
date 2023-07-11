from pathlib import Path

class Config:
    RANDON_SEED = 28 # Seed
    TEST_SIZE = 0.2
    ASSETS_PATH = Path("./assets")
    scripts_PATH = Path("./scripts")
    ORIGINAL_DATASET_FILE_PATH = ASSETS_PATH / "original_dataset" / "dt_rco.csv" # Dataset original
    DATASET_PATH = ASSETS_PATH / "data" # Dossier pour notre dataset
    DATASET_PREP = scripts_PATH / "preprocessing" # Nettoyage de notre dataset
    FEATURES_PATH = ASSETS_PATH / "features" # Dossier pour les features 
    MODELS_PATH = ASSETS_PATH / "models" # Dossier pour les modeles
    METRICS_FILE_PATH = ASSETS_PATH / "metrics.json" # Fichiers pour les mesures
