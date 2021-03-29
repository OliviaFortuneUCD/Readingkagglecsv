#Read the file

import pandas as pd
covid_vaccination = pd.read_csv("country_vaccinations.csv")


# Find the quantity of each vaccine combination used.

print(covid_vaccination['vaccines'].value_counts())