# backend/app/utils/data_processing.py
import pandas as pd

def process_tabular(file):
    df = pd.read_csv(file)
    df.to_csv('data.csv', index=False)  # Save the data for further use
    return df

def compute_statistics(df):
    statistics = {
        'mean': df.mean().to_dict(),
        'median': df.median().to_dict(),
        'mode': df.mode().iloc[0].to_dict(),
        'quartiles': df.quantile([0.25, 0.5, 0.75]).to_dict(),
        'outliers': df.apply(lambda x: x[(x < (x.mean() - 2 * x.std())) | (x > (x.mean() + 2 * x.std()))]).dropna().to_dict()
    }
    return statistics
