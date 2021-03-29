#Read the file

import pandas as pd
covid_vaccination = pd.read_csv("country_vaccinations.csv")
#Read hedings and 10 records

print(covid_vaccination.head(10))

#Print the headings and their details
print(covid_vaccination.info())

#print the values which are null

print(info_covid = covid_vaccination.isnull().sum())

#which country is using which vacine
covid_vaccination['country_vac'] = covid_vaccination['country'] + ' vaccine is used - ' +  covid_vaccination['vaccines']