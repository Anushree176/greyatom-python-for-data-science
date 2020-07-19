# --------------
# Importing header files
import numpy as np
import warnings

warnings.filterwarnings('ignore')

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Reading file
data = np.genfromtxt(path, delimiter=",", skip_header=1)
#Code starts here
new_record = np.asarray(new_record)
census = np.concatenate([data, new_record])
census.shape

age = census[:,0]
max_age = age.max()
min_age = age.min()
age_mean = age.mean()
age_std = age.std()
print(max_age)
print(min_age)
print(age_mean)
print(age_std)

race = census[:,2]
race_0 = race[race == 0]
len_0 = race_0.size
race_1 = race[race == 1]
len_1 = race_1.size
race_2 = race[race == 2]
len_2 = race_2.size
race_3 = race[race == 3]
len_3 = race_3.size
race_4 = race[race == 4]
len_4 = race_4.size
l = np.asarray([len_0,len_1,len_2,len_3,len_4])
minority_race = np.argmin(l)
minority_race

senior_citizens = census[census[:,0] > 60]
working_hours_sum = senior_citizens[:,6].sum()
senior_citizens_len = len(senior_citizens)
avg_working_hours = working_hours_sum/senior_citizens_len
print(avg_working_hours)

high = census[census[:,1] > 10]
low = census[census[:,1] <= 10]
avg_pay_high = high[:,7].mean()
avg_pay_low = low[:,7].mean()
print(round(avg_pay_high),2)
print(round(avg_pay_low),2)


