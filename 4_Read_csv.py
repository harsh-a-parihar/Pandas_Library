import pandas as pd
import numpy as np

# read csv file
df = pd.read_csv('data.csv', header=None)
print('\n', df.head())    # prints first 5 items
print('\n', df.shape)
print('\n', df.info())
df.columns = ['Duration', 'Pulse', 'Maxpulse', 'Calories']  # changes first row/heading
print('\n', df.head())
print('\n', df.tail())
print(df.dtypes)
# dates = pd.to_datetime(df['timestamp']).head()
# print(dates)
# df.set_index('something', inplace=True)   # set index to.

# max rows--------
print(pd.options.display.max_rows)  # ->60




