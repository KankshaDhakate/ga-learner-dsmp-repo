# --------------
# Import packages
import numpy as np
import pandas as pd
from scipy.stats import mode 
# code starts here
bank = pd.read_csv(path)
categorical_var = bank.select_dtypes(include = 'object')
print(categorical_var)
numerical_var = bank.select_dtypes(include='number')
print(numerical_var)


# code ends here


# --------------
# code starts here
banks = bank.drop(['Loan_ID'], axis = 1)
print(banks.isnull().sum())
bank_mode = banks.mode().iloc[0]
banks.fillna(value = bank_mode, inplace = True)
print(banks.head())
#code ends here


# --------------
# Code starts here
avg_loan_amount = banks.pivot_table(index=['Gender', 'Married', 'Self_Employed'], values = 'LoanAmount', aggfunc='mean')
print(avg_loan_amount)
# code ends here



# --------------




# code starts here

loan_approved_se = ((banks['Self_Employed']=='Yes') & (banks['Loan_Status']=='Y')).sum()

loan_approved_nse = ((banks['Self_Employed']=='No') & (banks['Loan_Status']=='Y')).sum()
Loan_Status = banks['Loan_Status'].count()
percentage_se = (loan_approved_se * 100 / Loan_Status)
percentage_nse = (loan_approved_nse * 100 / Loan_Status)
# code ends here
#filterinfDataframe = dfObj[(dfObj['Sale'] > 30) & (dfObj['Sale'] < 33) ]


# --------------
# code starts here
loan_term = banks["Loan_Amount_Term"].apply(lambda x: int(x) / 12)

big_loan_term = (loan_term >= 25).value_counts()[1]
print(big_loan_term)    

# code ends here


# --------------
# code starts here
loan_groupby = banks.groupby('Loan_Status')
loan_groupby = loan_groupby[['ApplicantIncome' , 'Credit_History']]
mean_values = loan_groupby.mean()


# code ends here


