#Read the file
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



covid_vaccination = pd.read_csv("country_vaccinations.csv")

#select the fields country etc...
bycountry= covid_vaccination[['country','total_vaccinations', 'people_vaccinated','people_vaccinated_per_hundred']].groupby(by='country').last()
bycountry

mean = bycountry.people_vaccinated_per_hundred.mean()
best = bycountry[bycountry.people_vaccinated > 3000000]

plt.figure(figsize=(10,8))
plt.bar(best.index, best.people_vaccinated_per_hundred, width=0.8, color='gold')
plt.plot(np.ones(15) * mean, linestyle='dashed', color='purple' , label='media mondiale')
plt.ylabel('person vaccinated per 100 ')
plt.xticks(rotation=45, ha='right')
plt.legend()
plt.grid()