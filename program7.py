#Read the file

import pandas as pd
covid_vaccination = pd.read_csv("country_vaccinations.csv")



# Obtain a dataframe of these data values for 'China'.

#df_china = covid_vaccination.loc[covid_vaccination['country'] == "China"]
#print(df_china)


# Obtain a dataframe of these data values for 'China'.

df_ireland = covid_vaccination.loc[covid_vaccination['country'] == "Ireland"]
print(df_ireland)
