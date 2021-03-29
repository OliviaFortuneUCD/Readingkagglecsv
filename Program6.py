#Read the file

import pandas as pd
covid_vaccination = pd.read_csv("country_vaccinations.csv")


# Find the maximum number of total vaccinations for each country and display them in descending order.

g1 = covid_vaccination.groupby(['country'])['total_vaccinations'].max().reset_index()
df2 = g1.sort_values(by='total_vaccinations', ascending = False, ignore_index = True)
df2

print(df2)