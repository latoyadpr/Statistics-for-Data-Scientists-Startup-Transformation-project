import codecademylib3
from sklearn import preprocessing
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np


# load in financial data
financial_data = pd.read_csv('financial_data.csv')

# code goes here

print(financial_data.head())
month = financial_data['Month']

plt.xlabel('Month')
plt.ylabel('Amount ($)')
plt.title('Revenue')

plt.clf()
#insert code to create plot here
#add labels to the plot here
plt.show()


expense_overview = pd.read_csv('expenses.csv')
print(expense_overview.head(7))

expense_categories = expense_overview['Expense']
proportions = expense_overview['Proportion']


plt.clf()
plt.pie(proportions, labels = expense_categories)
plt.title('Expense Categories')
plt.show()

plt.clf()
plt.pie(proportions, labels = expense_categories)
plt.title('Expense Categories')
plt.show()

plt.axis('Equal')
plt.tight_layout()


expense_categories = ['Salaries', 'Advertising', 'Office Rent', 'Other']
proportions = [0.62, 0.15, 0.15, 0.08]
plt.clf()
plt.pie(proportions, labels = expense_categories)
plt.title('Expense Categories')
plt.axis('Equal')
plt.tight_layout()
plt.show()


expense_categories = ['Salaries', 'Advertising', 'Office Rent', 'Other']
proportions = [0.62, 0.15, 0.15, 0.08]
plt.clf()
plt.pie(proportions, labels = expense_categories)
plt.title('Expense Categories')
plt.axis('Equal')
plt.tight_layout()
plt.show()


expense_cut = 'Salaries'

employees = pd.read_csv('employees.csv')  # Ensure this line is added to define 'employees'
print(employees.head())


sorted_productivity = employees.sort_values(by=['Productivity'])

employees_cut = sorted_productivity.head(100)
print(employees_cut)



transformation = 'standardization'

commute_times = employees['Commute Time']


print(commute_times.describe())


plt.clf()
plt.hist(commute_times)
plt.title("Employee Commute Times")
plt.xlabel("Commute Time")
plt.ylabel("Frequency")
plt.show()


commute_times_log = np.log(commute_times)


plt.hist(commute_times)

plt.hist(commute_times_log)

import matplotlib.pyplot as plt

plt.scatter(employees['Salary'], employees['Productivity'])
plt.xlabel('Salary')
plt.ylabel('Productivity')
plt.title('Relationship between Salary and Productivity')
plt.show()

correlation = employees[['Salary', 'Productivity']].corr()
print(correlation)
