#Read the file
import numpy as np
import pandas as pd
import seaborn as sns
import datetime
import calendar
import matplotlib.pyplot as plt

covid_vaccination = pd.read_csv("country_vaccinations.csv")

covid_vaccination.date = pd.to_datetime(covid_vaccination.date)
covid_vaccination['month']= covid_vaccination.date.dt.month
covid_vaccination['day']= covid_vaccination.date.dt.day

covid_vaccination['Week_day']=covid_vaccination.date.dt.weekday





ind = covid_vaccination.loc[covid_vaccination['country'] == 'Ireland']


plt.figure(figsize=(30,8))
sns.lineplot(x="date", y="total_vaccinations",data=ind)
plt.show()