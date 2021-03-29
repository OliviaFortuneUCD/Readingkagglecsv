#Read the file

import pandas as pd
covid_vaccination = pd.read_csv("country_vaccinations.csv")
#Read hedings and 10 records


#which country is using which vaccine
x = covid_vaccination['country_vac'] = covid_vaccination['country'] + ' vaccine is used - ' +  covid_vaccination['vaccines']
print(x)