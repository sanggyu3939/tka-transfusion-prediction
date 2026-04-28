from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier

def get_models():
    models = {
        "Logistic regression": LogisticRegression(
            max_iter=1000,
            class_weight="balanced",
            random_state=20260224
        ),
        "Random forest": RandomForestClassifier(
            n_estimators=500,
            min_samples_split=10,
            min_samples_leaf=5,
            class_weight="balanced",
            random_state=20260224
        ),
        "XGBoost": XGBClassifier(
            n_estimators=500,
            learning_rate=0.03,
            max_depth=3,
            subsample=0.8,
            colsample_bytree=0.8,
            eval_metric="logloss",
            random_state=20260224
        )
    }
    return models
