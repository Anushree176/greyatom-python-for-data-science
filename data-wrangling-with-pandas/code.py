# --------------
# Importing header files
import numpy as np
import pandas as pd
from scipy.stats import mode 
import warnings
warnings.filterwarnings('ignore')

#Reading file
bank_data = pd.read_csv(path)

#Code starts here
categorical_var = bank_data.select_dtypes(include = 'object')
print(categorical_var.shape)
numerical_var = bank_data.select_dtypes(include = 'number')
print(numerical_var.shape)

banks = pd.DataFrame(bank_data.drop(['Loan_ID'], axis=1))
print(banks.isnull().sum())
for col in banks.columns:
    banks[col].fillna(banks[col].mode()[0], inplace=True)

avg_loan_amount = pd.pivot_table(banks,
index = ['Gender', 'Married', 'Self_Employed'],
values = 'LoanAmount')
print(avg_loan_amount.head(5))


loan_approved_se = len(banks[(banks['Self_Employed']=="Yes") & (banks['Loan_Status']=='Y')])
loan_approved_nse = len(banks[(banks['Self_Employed']=="No") & (banks['Loan_Status']=='Y')])
percentage_se = (loan_approved_se/len(banks['Loan_Status']))*100
percentage_nse = (loan_approved_nse/len(banks['Loan_Status']))*100
print(percentage_se)
print(percentage_nse)

loan_term = banks['Loan_Amount_Term'].apply(lambda x : x/12)
big_loan_term = loan_term[loan_term >= 25]
print(len(big_loan_term))

loan_groupby = banks.groupby('Loan_Status')
mean_values = loan_groupby.mean()
print(mean_values)


