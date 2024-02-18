import pandas as pd
import numpy as np
# series----------
ser1 = pd.Series([1, 2, 3, 4, 5])
print(ser1)     # print series
print(type(ser1))   # ->.Series(pandas)
print(ser1.dtype)   # int64

print('\n')     # gap

# name the series----------
ser1.name = 'Common from 1 to 5'
print(ser1)     # prints series with name and dtype

print('\n')     # gap

# extract values as array--------
ser2 = pd.Series([10, 20, 30, 40, 50])
print(ser2[2])  # indexing
print(ser2.values)  # prints only the values
print(type(ser2.values))    # prints the type of values: numpy.ndarray
print(ser2.values.base)     # prints the base(view or copy): copy

print('\n')     # gap

# index of series-----------
ser3 = pd.Series([100, 200, 300, 400, 500])
ser3.name = 'Common number from 100 to 500'
print(ser3.index)   # prints the range of index(by default: 0,1,2,3,...)

print('\n')     # gap

# create index of series--------
ser3.index = {
    'hundred',
    'two_hundred',
    'three_hundred',
    'four_hundred',
    'five_hundred'
}
print(ser3)   # prints the series with particular index and value
print(ser3['three_hundred'])  # prints the value corresponding to it
print(ser3.iloc[-2])    # 'iloc' prints the value at given index
print(ser3.iloc[0: 4])  # slicing in series

print('\n')     # gap

# boolean selection---------
ser4 = pd.Series([10, 20, 30, 40, 50])
print(ser4 > 25)    # prints table with boolean result

# Series also applies all the arithmatic calculation
# Can also modify series easily



