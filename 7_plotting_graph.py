import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# how to plot graphs using pandas plot() function---------
covid_df = pd.DataFrame({
    'date': ['01-01-2020', '02-02-2020', '03-03-2020', '04-04-2020', '05-05-2020'],
    'new_cases': [100, 2000, 33894, 183039, 2000299], 
    'total_cases': [1000, 20000, 330000, 2400300, 30404030], 
    'total_deaths': [70, 200, 1000, 3029, 177897]
})
covid_df['date'] = pd.to_datetime(covid_df['date'])     # converted to datatime object
covid_df.set_index('date', inplace=True)

# simple graph
# covid_df['total_deaths'].plot()
# covid_df['total_cases'].plot()
# plt.show()  # shows graph

# bar graph
covid_df.total_deaths.plot(kind='bar')
plt.show()
