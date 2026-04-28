# TKA Transfusion Prediction

## Overview
This repository contains the code used in the study:

**"Machine Learning-Based Prediction of Postoperative Transfusion in Non-Anemic Patients Undergoing Total Knee Arthroplasty"**

The aim of this study was to develop and validate machine learning models to predict postoperative transfusion risk in patients undergoing total knee arthroplasty (TKA) with preoperative hemoglobin ≥11 g/dL.

---

## Methods
The following models were developed and compared:

- Logistic Regression
- Random Forest
- XGBoost

Model development included:
- Stratified train–validation split (80:20)
- 5-fold stratified cross-validation
- Independent validation set evaluation

Performance metrics:
- AUC (Area Under the ROC Curve)
- Accuracy
- Sensitivity
- Specificity
- Positive Predictive Value (PPV)
- Negative Predictive Value (NPV)
- F1-score

The optimal classification threshold was determined using the Youden index.

---

## Data
Due to institutional and ethical restrictions, the dataset used in this study cannot be publicly shared.

However, the code can be applied to similarly structured datasets.

---

## Reproducibility
All analyses were performed using:

- Python (version 3.10)
- scikit-learn
- XGBoost

---

## Usage

### 1. Install dependencies
```bash
pip install -r requirements.txt
