# --------------
#Header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#path of the data file- path
data = pd.read_csv(path)
#Code starts here 
data['Gender'].replace('-', 'Agender', inplace=True)
gender_count = data['Gender'].value_counts()
plt.bar(data['Gender'].unique(), gender_count)
plt.show()



# --------------
#Code starts here
alignment = data['Alignment'].value_counts()
plt.pie(alignment, labels=alignment, shadow=True)
plt.title("Character Alignment")
plt.show()


# --------------
#Code starts here
sc_df = data[['Strength', 'Combat']].copy()
sc_covariance = sc_df.cov().iloc[0,1]
sc_strength = data['Strength'].std()
sc_combat = data['Combat'].std()
sc_pearson = sc_covariance/(sc_strength*sc_combat)
print(sc_pearson)
ic_df = data[['Intelligence', 'Combat']].copy()
ic_covariance = ic_df.cov().iloc[0,1]
ic_intelligence = data['Intelligence'].std()
ic_combat = data['Combat'].std()
ic_pearson = ic_covariance/(ic_intelligence*ic_combat)
print(ic_pearson)



# --------------
#Code starts here
total_high = data['Total'].quantile(q=0.99)
super_best = data[data['Total'] > total_high]
super_best_names = list(super_best['Name'])
print(super_best_names)


#dfr[dfr['previous_loan_status'] == 'yes']['education']


# --------------
#Code starts here
fig, (ax_1, ax_2, ax_3) = plt.subplots(1,3)
ax_1.boxplot(data['Intelligence'])
ax_1.set_title('Intelligence')
ax_2.boxplot(data['Speed'])
ax_2.set_title('Speed')
ax_3.boxplot(data['Power'])
ax_3.set_title('Power')
plt.show()


