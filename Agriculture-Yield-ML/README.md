# Agriculture-Yield-ML

Research-grade ML pipeline for crop yield prediction and interpretability.

## Contents
- `data_prep.py` - ETL and feature engineering scripts
- `train.py` - training orchestration for RF / XGBoost / LSTM (config-driven)
- `evaluate.py` - evaluation metrics, cross-validation, SHAP explainability integration
- `notebooks/experiments.py` - runnable experiment notebook script
- `requirements.txt`

## Quick start
1. Prepare dataset in `data/` (CSV files) and ensure licensing allows use.
2. `pip install -r requirements.txt`
3. `python train.py --config configs/default.yaml`