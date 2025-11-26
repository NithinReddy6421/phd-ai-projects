import joblib, pandas as pd, numpy as np
import shap
def evaluate(model_path, data_path):
    model = joblib.load(model_path)
    df = pd.read_parquet(data_path)
    X = df.drop('yield', axis=1)
    explainer = shap.Explainer(model.predict, X)
    shap_values = explainer(X)
    print('SHAP summary shape:', shap_values.shape)

if __name__ == '__main__':
    evaluate('out/model.joblib', 'out/processed.parquet')