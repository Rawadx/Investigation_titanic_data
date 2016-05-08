import pandas as pd
import numpy as np

csv = pd.read_csv('titanic_data.csv')

survived = csv['Survived']
fare = csv['Fare']
pclass = csv['Pclass']
age = csv['Age']

# defining a function that calculate Pearson's correlation
def correlation(x,y):
    std_x=(x-x.mean()) / x.std(ddof=0)
    std_y=(y-y.mean()) / y.std(ddof=0)

    return (std_x * std_y).mean()

'''
Assigning correlations between survival and
1) Fare
2) Class
3) Age
'''
fare_class_corr = correlation(fare, pclass)
survived_fare_corr = correlation(survived, fare)
survived_class_corr = correlation(survived, pclass)
survived_age_corr = correlation(survived, age)

print "correlation between fare and class is: {0}".format(fare_class_corr)
print "correlation between survival and fare is: {0}".format(survived_fare_corr)
print "correlation between survival and class is: {0}".format(survived_class_corr)
print "correlation between survival and age is: {0}".format(survived_age_corr)


# plotting results in scatter plot
import matplotlib.pyplot as plt

lx = 'Survived'
fare_ly = 'Fare'
class_ly = 'Pclass'
age_ly ='Age'
 
def scatter_plot(lx, ly, x, y ):
    plt.title('Scatterplot')
    plt.xlabel(lx)
    plt.ylabel(ly)
    plt.scatter(x, y, c='blue')
    m, b = np.polyfit(x, y, 1)
    plt.plot(x, y, '.')
    plt.plot(x, m * x + b, '-')
    plt.show()
    
scatter_plot(fare_ly, class_ly, fare, pclass)
scatter_plot(lx, fare_ly, survived, fare)
scatter_plot(lx, class_ly, survived, pclass)
scatter_plot(lx, age_ly, survived, age)

