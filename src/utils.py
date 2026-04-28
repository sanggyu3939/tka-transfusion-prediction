import numpy as np
from sklearn.metrics import roc_auc_score

def get_optimal_threshold_youden(y_true, y_prob):
    thresholds = np.linspace(0, 1, 100)
    best_thresh = 0
    best_score = -1

    for t in thresholds:
        y_pred = (y_prob >= t).astype(int)
        sensitivity = ((y_pred == 1) & (y_true == 1)).sum() / (y_true == 1).sum()
        specificity = ((y_pred == 0) & (y_true == 0)).sum() / (y_true == 0).sum()
        score = sensitivity + specificity

        if score > best_score:
            best_score = score
            best_thresh = t

    return best_thresh
