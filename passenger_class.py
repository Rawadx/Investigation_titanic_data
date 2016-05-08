from __future__ import division
import pandas as pd

csv = pd.read_csv('titanic_data.csv')

survived = csv['Survived']
pclass = csv['Pclass'] 

# Getting the number of passengera from each passenger class
first_class = len(pclass[csv.Pclass ==1])
second_class = len(pclass[csv.Pclass ==2])
third_class = len(pclass[csv.Pclass ==3])


# Getting the number of survivors by passanger class
surv_first_class = survived[(csv.Survived ==1) & (csv.Pclass ==1)].count()
surv_second_class = survived[(csv.Survived ==1) & (csv.Pclass ==2)].count()
surv_third_class = survived[(csv.Survived ==1) & (csv.Pclass ==3)].count()

# Calculating the survivorship rate by passenger class
first_class_rate = round(surv_first_class/first_class, 4)*100
second_class_rate= round(surv_second_class/second_class, 4)*100
third_class_rate = round(surv_third_class/third_class, 4)*100


# plotting findings in a bar chart
import matplotlib.pyplot as plt

pass_class = {
              1:('First Class','r'), 
              2:('Second Class','g'), 
              3:('Third Class','b'),
             }

xval = [1., 2., 3.]

total_yval = [first_class, second_class, third_class]

surv_yval = [surv_first_class, surv_second_class, surv_third_class]

rate_yval= [first_class_rate, second_class_rate, third_class_rate]

total_title = 'Passengers Class Distribution' 
surv_title = 'Survivals Class Distribution' 
rate_title = 'Survival Rate Distribution by Passenger Class'
            
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

plot_bar(xval, total_yval, pass_class, total_title)
plot_bar(xval, surv_yval, pass_class, surv_title)
plot_bar(xval, rate_yval, pass_class, rate_title)
