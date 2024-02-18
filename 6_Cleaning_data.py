import pandas as pd
import numpy as np

# cleaning not null values
df = pd.DataFrame({
    'Sex': ['M', 'F', 'F', 'D', '?'],
    'Age': [20, 30, 400, 50, 840]
})
print(df)
print(df['Sex'].unique())   # find unique values
print(df['Sex'].value_counts())     # count values
# change values
print(df.replace({
    'Sex': {
        'D': 'F',
        'N': 'M',
        '?': 'M'
    }
}))
# or
print(df['Sex'].replace({'D': 'F', 'N': 'M'}))
# little hard correction in data
print(df[df['Age'] > 100])  # for ages more than 100
# how to change
df.loc[df['Age'] > 100, 'Age'] = df.loc[df['Age'] > 100, 'Age'] / 10
print(df)   # changed

print('\n')     # gap

# change duplicated values in the dataframe---------
df2 = pd.DataFrame({
    'Country': ['France', 'Brazil', 'Brazil', 'USA', 'India', 'India', 'India']
}, columns=['Name', 'Country'],
    index=['name1', 'name2', 'name3', 'name4', 'name5', 'name6', 'name7'])
# for values in Series
print(df2.duplicated())     # prints True for all last duplicate values
print(df2.duplicated(keep='last'))      # prints True for all first duplicate values
print(df2.duplicated(keep=False))   # prints True for all duplicate values
# drop for rows/columns in dataframe
print(df2.drop_duplicates())    # drops row has all the last duplicate values
print(df2.drop_duplicates(keep='last'))  # drops row has all first duplicate values
print(df2.drop_duplicates(keep=False))   # drops row  that has all duplicate values
# Note: You can use subset='column_name' as argument, you want to look for duplicates in.

print('\n')     # gap

# create a dataframe from raw data----------
data = pd.DataFrame({
    'data': ['1998?_M_US_6', '1990_F_India_10', '2020?_F_US_6', '2002_M_UK_8']
})
print(data)
print(data['data'].str.split('_'))  # prints array of split
data = data['data'].str.split('_', expand=True)
print(data)     # prints whole elements of into columns
data.columns = ['Year', 'Gender', 'Country', 'Total']
print(data)     # prints whole new dataframe with columns and rows
print(data['Year'].str.contains('\?'))  # prints True if in '\string', string is present
print(data['Country'].str.contains('U'))
# print(data['Country'].str.strip()     # to check space in ...
# print(data['Country'].str.replace(' ', '')    # to change space to not space
