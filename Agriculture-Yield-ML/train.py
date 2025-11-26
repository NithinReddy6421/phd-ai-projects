import argparse, yaml, joblib
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import cross_val_score
def train(cfg):
    df = pd.read_parquet(cfg['data']['processed_parquet'])
    X = df.drop(cfg['target'], axis=1)
    y = df[cfg['target']]
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    scores = cross_val_score(model, X, y, cv=5, scoring='neg_root_mean_squared_error')
    print('CV RMSE:', -scores.mean())
    model.fit(X, y)
    joblib.dump(model, cfg['output']['model_path'])
    print('Saved model to', cfg['output']['model_path'])

if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('--config', required=True)
    args = p.parse_args()
    cfg = yaml.safe_load(open(args.config))
    train(cfg)