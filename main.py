import pandas as pd
from matplotlib import pyplot as plt

data = pd.read_csv('countries.csv')
us = data[data.country == 'United States']
china = data[data.country == 'China']

plt.plot(us.year, us.population / 10**6)
plt.plot(china.year, china.population / 10**6,)
plt.title('Population Growth Over the Years: China vs. United States')
plt.legend(['United States', 'China'])
plt.xlabel('Year')
plt.ylabel('Population (in millions)')
plt.show()

df = pd.read_csv('cereal.csv', delimiter=';',skiprows=[1])

y = df['calories']
x = df['sodium']
plt.scatter(x,y)
plt.title('Correlation between Calories and Sodium Levels Amongst Popular Cereals')
plt.xlabel('Sodium (mg)')
plt.ylabel('Calories (cal)')
plt.show()