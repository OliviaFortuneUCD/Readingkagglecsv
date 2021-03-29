#Read the file

import pandas as pd
covid_vaccination = pd.read_csv("country_vaccinations.csv")

# Obtain a description of the dataset

covid_vaccination.describe()
print(covid_vaccination.describe())

# Examine the names and the count of each country.
print(covid_vaccination['country'].value_counts())

