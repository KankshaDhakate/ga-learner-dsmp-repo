# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data = pd.read_csv(path)
loan_status = data['Loan_Status'].value_counts()
plt.bar(loan_status.index, loan_status, color = "blue", edgecolor = 'black')
plt.show()
#Code starts here


# --------------





#Code starts here
property_and_loan = data.groupby(['Property_Area', 'Loan_Status']).size().unstack()
property_and_loan.plot(kind='bar', stacked=False)
plt.xlabel('Property Area')
plt.ylabel('Loan Status')
plt.xticks(rotation=45)
plt.show()


# --------------




#Code starts here
education_and_loan = data.groupby(['Education', 'Loan_Status']).size().unstack()
education_and_loan.plot(kind='bar', stacked = False)
plt.xlabel('Education Status')
plt.ylabel('Loan Status')
plt.xticks(rotation=45)


# --------------
#Code starts here
graduate = data[data['Education'] == "Graduate"]
not_graduate = data[data['Education'] == "Not Graduate"]
graduate['LoanAmount'].plot(kind='density', label='Graduate')
not_graduate['LoanAmount'].plot(kind='density', label='Not Graduate')











#Code ends here

#For automatic legend display
plt.legend()


# --------------
#Code starts here
fig, (ax_1, ax_2, ax_3) = plt.subplots(3,1, figsize=(10,10))

ax_1.scatter(data['ApplicantIncome'],data["LoanAmount"])
plt.title("Applicant Income")  

ax_2.scatter(data['CoapplicantIncome'],data["LoanAmount"])
plt.title("Coapplicant Income")

data['TotalIncome'] = data['ApplicantIncome'] + data['CoapplicantIncome']
ax_3.scatter(data['TotalIncome'],data["LoanAmount"])
plt.title('Total Income')

plt.show()


