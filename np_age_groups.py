from __future__ import division
import pandas as pd
from numpy import *

csv = pd.read_csv('titanic_data.csv')

# creating a numpy array of age column
np_age = csv['Age'].values 
# assigning empty fields to 0
nans= isnan(np_age)  
np_age[nans] = 0
# creating a numpy array of survived column
np_survived = csv['Survived'].values
np_age = csv['Age'].values


# getting number of passengers from each age group 
age_group_0 = len(np_age[(np_age == 0)])
age_group_1 = len(np_age[(np_age > 0) & (np_age <= 20)])
age_group_2 = len(np_age[(np_age > 20) & (np_age <= 40)])
age_group_3 = len(np_age[(np_age > 40) & (np_age <= 60)])
age_group_4 = len(np_age[(np_age > 60) & (np_age <= 80)])

# getting # of survivors from each age group
surv_age_group_0 = np_survived[np_age == 0].sum()
surv_age_group_1 = np_survived[(np_age >0) & (np_age <=20)].sum()
surv_age_group_2 = np_survived[(np_age >20) & (np_age <=40)].sum()
surv_age_group_3 = np_survived[(np_age >40) & (np_age <=60)].sum()
surv_age_group_4 = np_survived[(np_age >60) & (np_age <=80)].sum()

# Calculating the survivorship rate by age group
group_0_survivial_rate = round(surv_age_group_0/age_group_0, 4)*100
group_1_survival_rate= round(surv_age_group_1/age_group_1, 4)*100
group_2_survival_rate= round(surv_age_group_2/age_group_2, 4)*100
group_3_survival_rate= round(surv_age_group_3/age_group_3, 4)*100
group_4_survival_rate= round(surv_age_group_4/age_group_4, 4)*100

# investigating missing values
perc_missing_values = round(age_group_0/len(np_age), 4)*100
surv_perc_missing = round(surv_age_group_0/len(np_age), 4)*100


print 'There is {0} total missing age values and {1} missing age values from survivals'.format(age_group_0, surv_age_group_0)
print 'The sample data has {0}% of missing age values {1}% of which are survivors '.format(perc_missing_values, surv_perc_missing)

# plotting the results in a bar chart 
import matplotlib.pyplot as plt

age_groups = {
              1:('0-20','r'), 
              2:('21-40','g'), 
              3:('41-60','b'),
              4:('61-80','k'),
              5:('NAN', 'yellow'),
             }

xval = [1., 2., 3., 4., 5.]

total_yval = [age_group_1, age_group_2, age_group_3, age_group_4, age_group_0]

surv_yval = [surv_age_group_1, surv_age_group_2, surv_age_group_3,
             surv_age_group_4, surv_age_group_0]

rate_yval = [group_1_survival_rate, group_2_survival_rate,
        group_3_survival_rate, group_4_survival_rate, group_0_survivial_rate]

total_title = 'Passengers Age Group Distribution' 
surv_title = 'Survivals Age Group Distribution' 
rate_title = 'Survival Rate Distribution by Age Group'

def plot_bar(xval, yval, data, title):
    ax1 = plt.subplot(111)
    for j in range(len(xval)):
        ax1.bar(xval[j], yval[j], width=0.8, bottom=0.0, align='center',
                color=data[xval[j]][1], alpha=0.6,label=data[xval[j]][0])
    ax1.set_xticks(xval)
    ax1.set_xticklabels([data[i][0] for i in xval])
    ax1.set_title(title)
    #ax1.legend()
    plt.show()

plot_bar(xval, total_yval, age_groups, total_title)   
plot_bar(xval, surv_yval,age_groups, surv_title)
plot_bar(xval, rate_yval,age_groups, rate_title)

