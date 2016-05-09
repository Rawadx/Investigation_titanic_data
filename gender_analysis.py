from __future__ import division
import pandas as pd
import numpy as np

csv = pd.read_csv('titanic_data.csv')

survived = csv['Survived']
sex = csv['Sex']


male_passengers = sex[csv.Sex=='male'].count() #getting male passenger
female_passengers= sex[csv.Sex =='female'].count() #getting female passengers


male_survivors = survived[csv.Sex=='male'].sum() #getting male survivors
female_survivors= survived[csv.Sex =='female'].sum() #getting female survivors


male_survival_rate= male_survivors/male_passengers #getting male survival rate
female_survival_rate = female_survivors/female_passengers # getting female survival rate


print ('Male passengers constitute {0}%'
        ' of the passengers while females' 
          ' constitue {1}%').format(round(male_passengers/csv['Sex'].count(), 4)*100
                            , round(female_passengers/csv['Sex'].count(), 4)*100)



print ('Male survivors constitute {0}%'
        ' of the survivors while females' 
          ' constitue {1}%').format(round(male_survivors/csv['Survived'].sum(), 4)*100
                            , round(female_survivors/csv['Survived'].sum(), 4)*100)

print ('Male survival rate is {0}%'
        'while female survival rate'
          ' is {1}%').format(round(male_survival_rate, 4)*100
                            , round(female_survival_rate, 4)*100)

# plotting the results in pie charts
import matplotlib.pyplot as plt

# make the pie circular by setting the aspect ratio to 1
plt.figure(figsize=plt.figaspect(1))

passenger_data = [male_passengers, female_passengers]
survivor_data = [male_survivors, female_survivors]

labels = ['Male', 'Female']


def make_autopct(data):
    def my_autopct(pct):
        total = sum(data)
        val = int(round(pct*total/100.0))
        return '{p:.2f}%  ({v:d})'.format(p=pct,v=val)
    return my_autopct

plt.pie(passenger_data, labels=labels,autopct=make_autopct(passenger_data))
plt.title('Passengers by Gender')
plt.show()

plt.figure(figsize=plt.figaspect(1))
plt.pie(survivor_data, labels=labels,autopct=make_autopct(survivor_data))
plt.title('Survivors by Gender')
plt.show()


import matplotlib.pyplot as plt; plt.rcdefaults()
labels = ['Male', 'Female']
y_pos = np.arange(len(labels))
data = [male_survival_rate*100,female_survival_rate*100]
          
plt.barh(y_pos, data, align='center', alpha=0.4)
plt.yticks(y_pos, labels)
plt.xlabel('Survival Rate (%)')
plt.title('Survival Rate by Gender (%)')

plt.show()          








