import pandas as pd
import numpy as np

# create dataframes------------
df1 = pd.DataFrame({
    'Name': ['Harsh', 'Abhijit', 'Sumit', 'Robert'],
    'Marks': [100, 98, 98, 10],
    'Subjects': ['CSE', 'Maths', 'Reasoning', 'Quantum_physics']
}, columns=['Name', 'Marks', 'Subjects'])
print(df1)  # print the whole table/dataframe
print('\n', df1.values)     # prints all values
print('\n', df1.index)      # prints RangeIndex
print('\n', df1.info())     # prints all the info of dataframe
print('\n', df1.size)       # prints the size of dataframe
print('\n', df1.shape)      # prints shape of dataframe
print('\n', df1.describe())     # prints full arithmatic opps of dataframe
print('\n', df1.dtypes)     # prints all the dtype of elements
print('\n', df1.dtypes.value_counts())      # prints total number of values
print('\n', df1.sort_index(ascending=False))    # sorts index in descending order
print('\n', df1.sort_values('Marks', ascending=False))  # sorts value given in descending order

# group data and calculate sum(), mean(), count(), etc.
# dataframe.groupby('Column_name_you_want_to_group')['column1', 'column2', 'column3'].sum()/.mean()/etc.

# time_series (dtype: datetime)
# pd.to_datetime(series_of_dataframe)
# pd.DatetimeIndex(series_of_dataframe).year/.month/.day/.weekday

# merge two dataframes(data1 and data2) using one common column
# merged_df = data1.merge(data2, on='common_column_name')

# save_result in csv file
# 1st: result_df = merged_df[['column1', 'column2', 'column3', ...]]
# 2nd: result_df.to_csv('result.csv', index=False)      # file saved

print('\n')     # gap

# indexing, slicing, and selection----------
df2 = pd.DataFrame({
    'Population': [553.32, 222.23, 32.32, 129.43, 403.30],
    'GDP': [393929, 304040, 303045, 30030, 30020],
    'Continent': ['Asia', 'North-America', 'Australia', 'South-America', 'Africa']
}, columns=['Population', 'GDP', 'Continent'], index=[
    'India',
    'Canada',
    'Melbourne',
    'Brazil',
    'Egypt'
])
print(df2.loc['India'])
print(df2.iloc[2])
print(df2['Population'])

print('\n')     # gap

# extracting data from the dataframe
# datafram.at[index, 'column_name']

print('\n')     # gap

# dropping stuffs
print(df2.drop(['Brazil']))     # by index/row
print(df2.drop(columns=['GDP']))    # by column
