# --------------
import pandas as pd
import scipy.stats as stats
import math
import numpy as np
import warnings

warnings.filterwarnings('ignore')
#Sample_Size
sample_size=2000

#Z_Critical Score
z_critical = stats.norm.ppf(q = 0.95)  

# path        [File location variable]

#Code starts here
data = pd.read_csv(path)
data_sample = data.sample(n=2000, random_state=0)
sample_mean = data_sample['installment'].mean()
sample_std = data_sample['installment'].std()
a = sample_size ** 0.5
# print(type(z_critical))
# print(type(sample_std))
# print(type(a))
margin_of_error = z_critical * (sample_std/a)
confidence_interval = (sample_mean - margin_of_error, sample_mean + margin_of_error)
true_mean = data['installment'].mean()
print(confidence_interval)
print(true_mean)


# --------------
import matplotlib.pyplot as plt
import numpy as np

#Different sample sizes to take
sample_size=np.array([20,50,100])

#Code starts here
fig, axes = plt.subplots(3,1)
for i in range(len(sample_size)):
    m = list()
    for j in range(1000):
        m.append(data['installment'].sample(n=sample_size[i]).mean())

    mean_series = pd.Series(m)
    plt.hist(mean_series)
    plt.show()


# --------------
#Importing header files

from statsmodels.stats.weightstats import ztest

#Code starts here
# x = data['int.rate'].str.strip('%').astype(float)
# print(x)
# data['int.rate'] = x/100
# print(data['int.rate'])

data['int.rate'] = (data['int.rate'].str.replace('%', '').astype(float))/100
# print(data['int.rate'])

z_statistic, p_value = ztest(data[data['purpose']=='small_business']['int.rate'],value=data['int.rate'].mean(), alternative='larger')
print("Z-statistics = ",z_statistic)
print("p-value = ",p_value)

if p_value < 0.05:
    print("Reject")
else:
    print("Accept")


# --------------
#Importing header files
from statsmodels.stats.weightstats import ztest

#Code starts here
z_statistic, p_value = ztest(x1 = data[data['paid.back.loan']=='No']['installment'], x2 = data[data['paid.back.loan']=='Yes']['installment'])

print('Z-statistics = ', z_statistic)
print('p-value = ', p_value)

if p_value < 0.05:
    print("Reject")
else:
    print("Accept")


# --------------
#Importing header files
from scipy.stats import chi2_contingency

#Critical value 
critical_value = stats.chi2.ppf(q = 0.95, # Find the critical value for 95% confidence*
                      df = 6)   # Df = number of variable categories(in purpose) - 1


#Code starts here
yes = data[data['paid.back.loan'] == 'Yes']['purpose'].value_counts()
no = data[data['paid.back.loan'] == 'No']['purpose'].value_counts()

observed = pd.concat([yes.transpose(), no.transpose()], axis = 1, keys = ['Yes', 'No'])
print(observed)
chi2, p, dof, ex = chi2_contingency(observed)

if chi2 > critical_value:
    print("Reject the Null Hypothesis.")
else:
    print("Do not reject the Null Hypothesis.")


