# Import necessary libraries
import numpy as np
import pandas as pd

# Create a pandas Series with custom index
series = pd.Series([267,221,307,228], index=['Inng1', 'Inng2', 'Inng3', 'Inng4'])
print(series)  # Print the Series

# Create a dictionary with employee data
emp_data = {
    'DAS_ID': ['A825825', 'A825826', 'A825827', 'A825828'],
    'Name': ['John', 'Jane', 'Doe', 'Smith'],
    'Age': [28, 34, 29, 40],
    'Salary': [50000, 60000, 55000, 70000],
    'Department': ['HR', 'Finance', 'IT', 'Marketing'],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}

# Convert the dictionary to a pandas DataFrame
df = pd.DataFrame(emp_data)
print(df)  # Print the DataFrame

print(df['Name'])   # Print the 'Name' column
print(df[df['Salary'] <= 55000])  # Print rows where Salary is less than or equal to 55000

# Read a CSV file named 'sample.csv' into a DataFrame
df1 = pd.read_csv('sample.csv')

print(df1)  # Print the DataFrame loaded from CSV
print(df1['sal'])  # Print the 'sal' column from the DataFrame
print(df1[df1['sal'] > 5500])  # Print rows where 'sal' column is greater than 5500