import os
import pandas as pd
import numpy as np
import numpy_financial as npf
import matplotlib.pyplot as plt
import seaborn as sns


file_path = os.path.join(os.path.dirname('C:\\Users\\gribh\\Downloads\\FIN3009 Portfolio'), 'Nordea_stabil_avkastning.csv')


df = pd.read_csv(file_path, sep=',', encoding='utf-8')

def set_datetime(dataframe):
    dataframe['Date'] = pd.to_datetime(dataframe['Date'])
    dataframe.set_index('Date', inplace = True)

set_datetime(df)

TRADING_DAYS = 252
returns = np.log(df['Close']/df['Close'].shift(1))
returns.fillna(0, inplace=True)
df['Volatility'] = returns.rolling(window=TRADING_DAYS).std()*np.sqrt(TRADING_DAYS)
print(df.tail())

new_df = df.dropna()
new_df.reset_index(0)
print(new_df)
new_df.info() 

new_returns = np.log(new_df['Adj Close']/new_df['Adj Close'].shift(1))
new_returns.fillna(0, inplace=True)
print(new_returns)
