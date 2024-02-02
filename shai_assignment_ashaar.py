# -*- coding: utf-8 -*-
"""ShAI_Assignment_ashaar.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xq-VUoZV2hQQRoB19uxYlq1L7S10LF1L

#About Dataset
salaries dataset generally provides information about the employees of an organization in relation to their compensation. It typically includes details such as how much each employee is paid (their salary), their job titles, the departments they work in, and possibly additional information like their level of experience, education, and employment history within the organization.

# Features
- 'Id'
- 'EmployeeName'
- 'JobTitle'
- 'BasePay'
- 'OvertimePay'
- 'OtherPay'
- 'Benefits'
- 'TotalPay' -> salary
- 'TotalPayBenefits'
- 'Year'
- 'Notes'
- 'Agency'
- 'Status'

# Tasks

1. **Basic Data Exploration**: Identify the number of rows and columns in the dataset, determine the data types of each column, and check for missing values in each column.

2. **Descriptive Statistics**: Calculate basic statistics mean, median, mode, minimum, and maximum salary, determine the range of salaries, and find the standard deviation.

3. **Data Cleaning**: Handle missing data by suitable method with explain why you use it.

4. **Basic Data Visualization**: Create histograms or bar charts to visualize the distribution of salaries, and use pie charts to represent the proportion of employees in different departments.

5. **Grouped Analysis**: Group the data by one or more columns and calculate summary statistics for each group, and compare the average salaries across different groups.

6. **Simple Correlation Analysis**: Identify any correlation between salary and another numerical column, and plot a scatter plot to visualize the relationship.

8. **Summary of Insights**: Write a brief report summarizing the findings and insights from the analyses.

# Very Important Note
There is no fixed or singular solution for this assignment, so if anything is not clear, please do what you understand and provide an explanation.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import numpy as np

# Load your dataset
df = pd.read_csv('/content/Salaries.csv')
df.head()

"""### Basic Data Exploration


"""

print(len(df.columns)) #How many coulmns , what is it
df.columns

df.shape # number columns and row

#df.dtypes
df.info() #  types of each column check for missing values

df.isnull().sum() #check for missing values

for c in df.columns:
  print(f'{c}\t' ,len(df[c].unique()) )

df.duplicated().sum()

"""### Descriptive Statistics"""

df.describe()

df.describe(include='object')

"""### Data Cleaning

drop column :
1.  not have any data
2.   all data have the same value
3. Does not provide important information for analysis
"""

df.drop(["Status","Notes"] , axis=1 , inplace=True) # ther are not any data in these column so drop it

print(df['Agency'].unique()) # all are from "San Francisco " thats dont get mater in anylisis
print(df['Year'].unique())

df.drop( "Agency", axis=1 , inplace=True)

df.drop(['EmployeeName','Id'] ,axis=1, inplace=True )  #not important information

"""Dealing with this missing data
1. BasePay ---->               609
2. Benefits --->            36163
3. OvertimePay  ---->            4
4. OtherPay  ---->               4

"""

#TotalPayBenefits	= Benefits	+TotalPay
#TotalPay =BasePay + OvertimePay + OtherPay

#data have small miss value
df.dropna(subset=['OvertimePay'], inplace=True)
df.dropna(subset=['OtherPay'], inplace=True)

# fill data have mich miss data acoording to the relation
##TotalPay =BasePay + OvertimePay + OtherPay 0------>BasePay = TotalPay - OvertimePay - OtherPay
df['BasePay'].fillna(df['TotalPay'] - df['OvertimePay'] - df['OtherPay'] , inplace=True)

#TotalPayBenefits	= Benefits	+TotalPay ----> Benefits = TotalPayBenefits -TotalPay
df['Benefits'].fillna(df['TotalPayBenefits'] - df['TotalPay']  , inplace=True)

df

df.isnull().sum()

"""### **Basic Data Visualization**"""

#TotalPay = salaries
# Plotting histogram
plt.figure(figsize=(10, 6))
plt.hist(df['TotalPay'], bins=20,color='pink', edgecolor='black')

# Adding labels and title
plt.title('Salary Distribution Histogram')
plt.xlabel('Salaries')
plt.ylabel('Frequency')

# Display the histogram
plt.show()

#df['JobTitle'].unique().sum()
#df[df['JobTitle'].duplicated()]
df['Department'] = df['JobTitle'].str.extract(r'\((.*?)\)')
df['Department'].unique()

df['JobTitle'] = df['JobTitle'].str.lower()
#df['JobTitle'] = df['JobTitle'].str.replace(r'[^()\s]', '', regex=True)
#df['Department'] = np.where(df['JobTitle'].str.contains('Police', case=False), 'POLICE DEPARTMENT', '')
#athor= df['JobTitle'].str.extract(r'\((.*?)\)')
df['Department'] = np.where(df['JobTitle'].str.contains('Police', case=False), 'police department', df['Department'])
df['Department'] = np.where(df['JobTitle'].str.contains('fire', case=False), 'fire department', df['Department'])
df['Department'] = np.where(df['JobTitle'].str.contains('civil', case=False), 'Civil & Criminal', df['Department'])
df['Department'] = np.where(df['JobTitle'].str.contains('cvl', case=False), 'Civil & Criminal', df['Department'])
df['Department'] = np.where(df['JobTitle'].str.contains('mfcc', case=False), 'MFCC', df['Department'])
df['Department'] = np.where(df['JobTitle'].str.contains('sfers', case=False), 'SFERS', df['Department'])
df['Department'] = np.where(df['JobTitle'].str.contains('seasonal', case=False), 'SEASONAL', df['Department'])
df.isnull().sum()
df['Department'].unique()
df[df['Department']== 'head v']
df[df['JobTitle'].str.contains('department', case=False, na=False)]



department_counts = df['Department'].value_counts()

# Plotting a pie chart
plt.figure(figsize=(8, 8))
plt.pie(department_counts, labels=department_counts.index, autopct='%1.1f%%', startangle=90)
plt.show()

"""### **Simple Correlation Analysis**"""

df.corr()

"""# Good Luck!"""

import seaborn as sns
import matplotlib.pyplot as plt

# Calculate the correlation matrix
correlation_matrix = df.corr()

# Create a heatmap of the correlation matrix with distinct positive and negative colors
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=.5, center=0)
plt.title('Correlation Heatmap')
plt.show()

#BasePay	OvertimePay	OtherPay	Benefits	TotalPay	TotalPayBenefits	Year	Notes	Agency	Status
plt.figure(figsize=(8, 6))
sns.scatterplot(x='TotalPay', y='Benefits', data=df, color='blue')

# Adding labels and title
plt.title('Scatter Plot: Salary vs Benefits')
plt.xlabel('Salary')
plt.ylabel('Benefits')

# Display the plot
plt.show()

import seaborn as sns
sns.pairplot(df ,  x_vars=["TotalPay"])

plt.show()

"""### **Grouped Analysis**"""

# Group by 'Department' and calculate average total pay for each group
grouped_department_total_pay = df.groupby('Department')['TotalPay'].mean().reset_index()

# Group by 'Department' and 'Year' and calculate average total pay for each group
grouped_department_total_pay_across_years = df.groupby(['Department', 'Year'])['TotalPay'].mean().reset_index()

# Group by 'Year' and calculate average total pay for each group
grouped_total_pay_with_years = df.groupby('Year')['TotalPay'].mean().reset_index()


grouped_department_benefits = df.groupby('Department')['Benefits'].mean().reset_index()

# Display the grouped data
print("Average Total Pay by Department:")
print(grouped_department_total_pay)

print("\nAverage Total Pay by Department Across Years:")
print(grouped_department_total_pay_across_years)

print("\nAverage Total Pay Across Years:")
print(grouped_total_pay_with_years)

# Bar plot to compare average total pay across different departments
plt.figure(figsize=(12, 4))

plt.subplot(1, 3, 1)
sns.barplot(x='Department', y='TotalPay', data=grouped_department_total_pay, palette='viridis')
plt.title('Average Total Pay by Department')
plt.xlabel('Department')
plt.ylabel('Average Total Pay')

# Bar plot to compare average total pay across different departments across years
plt.subplot(1, 3, 2)
sns.barplot(x='Department', y='TotalPay', hue='Year', data=grouped_department_total_pay_across_years, palette='viridis')
plt.title('Average Total Pay by Department Across Years')
plt.xlabel('Department')
plt.ylabel('Average Total Pay')

# Line plot to visualize the trend of average total pay across years
plt.subplot(1, 3, 3)
sns.lineplot(x='Year', y='TotalPay', data=grouped_total_pay_with_years, marker='o', color='purple')
plt.title('Average Total Pay Across Years')
plt.xlabel('Year')
plt.ylabel('Average Total Pay')

plt.tight_layout()
plt.show()

# Bar plot to compare average benefits across different departments

sns.barplot(x='Department', y='Benefits', data=grouped_department_benefits, palette='viridis')
plt.title('Average Benefits by Department')
plt.xlabel('Department')
plt.ylabel('Average Benefits')
plt.show()