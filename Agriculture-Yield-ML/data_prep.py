import pandas as pd, argparse, os
def prepare(csv_in, out_dir):
    df = pd.read_csv(csv_in)
    # example feature engineering: date -> month, lag features
    if 'date' in df.columns:
        df['date'] = pd.to_datetime(df['date'])
        df['month'] = df['date'].dt.month
    os.makedirs(out_dir, exist_ok=True)
    df.to_parquet(os.path.join(out_dir, 'processed.parquet'))
    print('Saved processed data to', out_dir)

if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('--csv', required=True)
    p.add_argument('--out', default='out')
    args = p.parse_args()
    prepare(args.csv, args.out)