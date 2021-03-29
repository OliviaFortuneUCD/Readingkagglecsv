#Read the file

import pandas as pd
import matplotlib as mpl

covid_vaccination = pd.read_csv("country_vaccinations.csv")



df_ireland = covid_vaccination.loc[covid_vaccination['country'] == "Ireland"]
print(df_ireland)



df_ireland.plot(x = 'date', y = 'total_vaccinations', kind='line')

