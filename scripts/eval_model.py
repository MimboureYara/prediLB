from os import remove
import pickle # Serialiser des objets (y comporis des modeles)
import json 
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.metrics import f1_score, confusion_matrix, classification_report
from sklearn.model_selection import learning_curve
import pandas as pd
from pandas.core.algorithms import mode
from sklearn.metrics import mean_squared_error, mean_absolute_error

from config import Config

x_test = pd.read_csv(str(Config.FEATURES_PATH / "test_features.csv"))
y_test = pd.read_csv(str(Config.FEATURES_PATH / "test_labels.csv"))
y_test = y_test.to_numpy().ravel()

# Restaurer le modèle
model = pickle.load(open(str(Config.MODELS_PATH / "model.pk"), mode='rb'))

# https://scikit-learn.org/0.15/modules/model_evaluation.html (regression)
r_squared = model.score(x_test, y_test)

y_pred = model.predict(x_test)
rmse = mean_squared_error(y_test, y_pred)
rmae = mean_absolute_error(y_test, y_pred)

with open(str(Config.METRICS_FILE_PATH), mode='w') as f:
    json.dump(dict(r_squared=r_squared, rmse=rmse, rmae=rmae), f)
