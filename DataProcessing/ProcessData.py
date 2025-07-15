import pandas as pd
import numpy as np

from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.impute import SimpleImputer

#data

data = {
    'Name': ['A825662', 'A825663', 'A825664', np.nan],
    'Age': [25, np.nan, 30, 22],
    'Salary': [50000, 60000, np.nan, 45000],
    'Gender': ['F', 'M', 'M', 'F'],
    'Department': ['HR', 'Finance', 'IT', 'HR'],
    'Purchased_Product': [1, 0, 1, 0]
}
df = pd.DataFrame(data)
print(df)
# processing missing values
imputer = SimpleImputer(strategy='mean')
df[['Age', 'Salary']] = imputer.fit_transform(df[['Age', 'Salary']])

print(df)

df['Name'] = df['Name'].fillna(df['Name'].mode()[1])   
print(df)

# encoding categorical variables
le = LabelEncoder()
df['Gender'] = le.fit_transform(df['Gender'])   # Male: 0, Female: 1
df['Department'] = le.fit_transform(df['Department'])  # HR: 0, Finance: 1, IT: 2
print(df)

df = df.drop_duplicates(subset=['Name'], keep='last')
print(df)

#  preprocessed data
preprocessed_data = df.copy()
# scaling numerical features
scaler = StandardScaler()
preprocessed_data[['Age', 'Salary']] = scaler.fit_transform(preprocessed_data[['Age', 'Salary']])
print(preprocessed_data)
# saving preprocessed data to a CSV file
preprocessed_data.to_csv('preprocessed_data.csv', index=False)
df.to_csv('original_data.csv', index=False)
print(preprocessed_data)