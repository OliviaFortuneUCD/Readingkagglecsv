#Read the file

import pandas as pd
import matplotlib as mpl

covid_vaccination = pd.read_csv("country_vaccinations.csv")





x = covid_vaccination['total_vaccinations']
y = covid_vaccination['people_vaccinated']
ax = covid_vaccination.plot(figsize = (15,5),title = "World Covid-19 Vaccinations")
ax.set_xlabel('countries')
ax.set_ylabel('values')

