import os
import pandas as pd
import numpy as np

file_path = os.path.join(os.path.dirname(__file__), 'Nordea_stabil_avkastning.csv')


df = pd.read_csv(file_path, sep=',', encoding='utf-8')


TRADING_DAYS = 252
returns = np.log(df['Close']/df['Close'].shift(1))
returns.fillna(0, inplace=True)
df['Volatility'] = returns.rolling(window=TRADING_DAYS).std()*np.sqrt(TRADING_DAYS)
print(df.tail())