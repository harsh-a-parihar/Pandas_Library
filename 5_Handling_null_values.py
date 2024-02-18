import pandas as pd
import numpy as np

# using below functions you can find null values--------
# pd.isnull(np.nan) -> pd.notnull(np.nan)
# pd.isnull(None)   -> pd.notnull(None)
# pd.isna(np.nan)   -> pd.notna(np.nan)
# pd.isna(None)     -> pd.notna(None)
# all these are immutable, this will no change any original dataframe/Series unless (inplace=True)

print(pd.isnull(pd.Series([1, 2, np.nan, 4])))  # prints True if null value present
print(pd.isna(pd.Series([10, 20, None, 40])))
print(pd.notnull(pd.Series([1, 2, np.nan, 4]))) # prints True if null value not present
print(pd.notna(pd.Series([10, 20, None, 40])))

print('\n')     # gap

# count null and notnull values in the series----------
df = pd.Series([1, 2, 3, np.nan, 5, None, 0, np.nan])
print(pd.isnull(df).sum())      # prints sum all null values
print(pd.notnull(df).sum())     # prints sum of all not null values

print('\n')     # gap

# filter the data---------
df2 = pd.Series([100, np.nan, 3, None, None, 0, 10])
print(df2[pd.isnull(df2)])  # prints all the values which are null
print(df2[pd.notnull(df2)])     # prints all the values which are not null
# we can also do;
print(df2.isnull())
print(df2.notnull())

print('\n')     # gap

# one straight method for filtering notnull data is dropna()--------
df3 = pd.Series([1, 2, np.nan, 4, None, 6, 7, None, None, 10])
print(df3.dropna())     # prints all the values which are not null

print('\n')     # gap

# drop the row contains any, all, or thresh value null----------
df0 = pd.DataFrame({
    'name': ['harsh', np.nan, 'sumit', None, 'Rajnish'],
    'state': ['Uttar Pradesh', None, 'Uttar Pradesh', np.nan, 'Bihar'],
    'Marks': [100, 10, 100, 90, 100],
    'Mo.no': [7389274388, None, 2888882834, 3882848838, 3884839389]
}, columns=['name', 'state', 'Marks', 'Mo.no'])
print('\n', df0.dropna(how='all'))
print('\n', df0.dropna(how='any'))
print('\n', df0.dropna(thresh=2))

print('\n')     # gap

# filling null values
print('\n', df0.fillna(0))    # fills the null values
print('\n', df0.fillna(method='ffill'))   # fills the null with predicted value from front
print('\n', df0.fillna(method='bfill'))   # fill the null with predicted value from back
# for axis=0 -> vertically filling works
# for axis=1 -> horizontally filling works


