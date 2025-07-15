import pandas as pd
import numpy as np
from scipy.stats import zscore


data = {
    'Age' : [22,25,23,24,26,27,28,29,30,31,2025], # 2020 & 2025 are outliers
    'Salary' : [50000,60000,55000,58000,62000,63000,70000,72000,75000,80000,1000000] # 1000000 & 2000000 are outliers
}

dataframe1 = pd.DataFrame(data)
print(dataframe1)

z_scores = np.abs(zscore(dataframe1[['Age', 'Salary']]))

print("Z-scores:\n", z_scores)

# threshold = 3
dataframe1['Outlier'] = (z_scores > 3).any(axis=1)

print("Data with Outliers:\n", dataframe1[dataframe1['Outlier']])

#  Using IQR method to detect outliers
Q1 = dataframe1[['Age', 'Salary']].quantile(0.25)
Q3 = dataframe1[['Age', 'Salary']].quantile(0.75)
IQR = Q3 - Q1
print("IQR:\n", IQR)

outliers_iqr = ((dataframe1[['Age', 'Salary']] < (Q1 - 1.5 * IQR)) | 
                (dataframe1[['Age', 'Salary']] > (Q3 + 1.5 * IQR))).any(axis=1)

dataframe1['Outlier_IQR'] = outliers_iqr
print("Data with Outliers using IQR:\n", dataframe1[dataframe1['Outlier_IQR']])


# Remove
dataframe1_Cleaned = dataframe1[dataframe1['Outlier'] == False].drop(['Outlier', 'Outlier_IQR'], axis=1)

print("Cleaned Data without Outliers:\n", dataframe1_Cleaned)

