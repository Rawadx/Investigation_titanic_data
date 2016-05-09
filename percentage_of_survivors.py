
from __future__ import division
import pandas as pd



csv = pd.read_csv('titanic_data.csv')

passengers = csv['Survived'].count() #getting the number of passengers
survivals = csv['Survived'].sum() #getting the number of survivors


# Calculating the number of survivors rounded to 2 decimal numbers
percentage_survived = round(survivals/ passengers, 4)*100 
percentage_victims = 100 - percentage_survived
    
print ' {0}% of the passangers survived while {1}% did not'.format(percentage_survived, percentage_victims) 

#plotting the results in a pie chart
import matplotlib.pyplot as plt

# make the pie circular by setting the aspect ratio to 1
plt.figure(figsize=plt.figaspect(1))
data = [percentage_survived, percentage_victims]
labels = ['Survived', 'Victims']

def make_autopct(data):
    def my_autopct(pct):
        total = sum(data)
        val = int(round(pct*total/100.0))
        return '{p:.2f}%  ({v:d})'.format(p=pct,v=val)
    return my_autopct

plt.pie(data, labels=labels,autopct=make_autopct(data))
plt.show()
