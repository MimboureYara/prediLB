import pickle # Serialiser des objets (y comporis des modeles)
import pandas as pd
#from sklearn.ensemble import RandomForestRegressor
from sklearn.neighbors import KNeighborsClassifier
from config import Config

from sklearn.pipeline import make_pipeline
from sklearn.feature_selection import SelectKBest, f_classif
#from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import precision_recall_curve
from sklearn.preprocessing import PolynomialFeatures, StandardScaler

Config.MODELS_PATH.mkdir(parents=True, exist_ok=True)

x_train = pd.read_csv(str(Config.FEATURES_PATH / "train_features.csv"))
y_train = pd.read_csv(str(Config.FEATURES_PATH / "train_labels.csv"))

# Entrainement du model
#model = RandomForestRegressor(n_estimators=150, max_depth=6, random_state=Config.RANDON_SEED)
#model = KNeighborsClassifier(n_estimators=150, max_depth=6, random_state=Config.RANDON_SEED)
preprocessor = make_pipeline(PolynomialFeatures(2, include_bias=False),SelectKBest(f_classif,k=10))
#model = make_pipeline(preprocessor, StandardScaler(), KNeighborsClassifier())
model = make_pipeline(preprocessor, StandardScaler(), SVC(random_state=0))

#model.fit(X_train, y_train.to_numpy().ravel()) # e.g. array([[1], [0]]).ravel() = array([1, 0])
#model.fit(x_train, y_train)

# Enregisrement du model
pickle.dump(model, open(str(Config.MODELS_PATH / "model.pk"), mode='wb'))