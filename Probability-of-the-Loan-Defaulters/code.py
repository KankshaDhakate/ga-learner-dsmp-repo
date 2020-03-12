# --------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# p_a = len(df[df['fico']> 700]) / len(df)
# p_b = len(df[df['purpose'] == 'debt_consolidation']) / len(df)
# df1 = df[df['purpose'] == 'debt_consolidation']
# p_a_b = len(df1[df1['fico']> 700]) / len(df1)

# code starts here
df = pd.read_csv(path)
x = len(df[df['fico']>700])
p_a = x/len(df)

df1 = df[df['purpose'] == 'debt_consolidation']

y = len(df1[df1['purpose'] == 'debt_consolidation'])
p_b = y/len(df)

p_a_b = len(df1[df1['fico']> 700]) / len(df1)

if p_a_b == p_a:
    result = True
else:
    result = False

print(result)

# code ends here


# --------------
# code starts here
prob_lp = df[df['paid.back.loan'] == 'Yes'].shape[0]/df.shape[0]
prob_cs = df[df['credit.policy'] == 'Yes'].shape[0]/df.shape[0]

new_df = df[df['paid.back.loan'] == 'Yes']
prob_pd_cs = new_df[new_df['credit.policy'] == 'Yes'].shape[0]/new_df.shape[0]

bayes = (prob_pd_cs*prob_lp)/prob_cs
print(bayes)

# code ends here

# prob_lp = df[df['paid.back.loan'] == 'Yes'].shape[0] / df.shape[0]
# prob_lp

# # probability of the credit policy is Yes
# prob_cs = df[df['credit.policy'] == 'Yes'].shape[0]  / df.shape[0]
# prob_cs
# # create new dataframe for paid.back.loan == 'Yes'
# new_df = df[df['paid.back.loan'] == 'Yes']

# # Calculate the P(B|A)
# prob_pd_cs = new_df[new_df['credit.policy'] == 'Yes'].shape[0] / new_df.shape[0]

# prob_pd_cs

# # bayes theorem 

# bayes = (prob_pd_cs * prob_lp)/ prob_cs

# # bayes
# bayes


# --------------
# code starts here
df.purpose.value_counts(normalize = True).plot(kind='bar')
df1 = df[df['paid.back.loan'] == 'No']
df1['purpose'].value_counts(normalize = True).plot(kind='bar')
# code ends here


# --------------
# code starts here
inst_median = df['installment'].median()
inst_mean = df['installment'].mean()
plt.hist(df.installment, color = 'green')
plt.hist(df['log.annual.inc'])
plt.show()
# code ends here


