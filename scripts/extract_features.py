# Considerer train.csv et test.csv
# Extraire les caracteriques qui nous intereste
# Enregistrer

import pandas as pd

from config import Config

Config.FEATURES_PATH.mkdir(parents=True, exist_ok=True)

df_train = pd.read_csv(str(Config.DATASET_PATH / "train.csv"))
df_test = pd.read_csv(str(Config.DATASET_PATH / "test.csv"))

features = ['SEXE', 'MassAbdo', 'AttH', 'AttMen', 'Gangl', 'Stad']
def extract_features(df):
    return df[features]

train_features = extract_features(df_train)
test_features = extract_features(df_test)

# Enregistrement des features pour train et test
train_features.to_csv(str(Config.FEATURES_PATH / "train_features.csv"), index=None)
test_features.to_csv(str(Config.FEATURES_PATH / "test_features.csv"), index=None)

# Enregistrement des labels pour train et test
df_train.to_csv(str(Config.FEATURES_PATH / "train_labels.csv"), index=None)
df_test.to_csv(str(Config.FEATURES_PATH / "test_labels.csv"), index=None)