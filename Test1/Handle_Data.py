import pandas as pd

data = {
    'name': ['Giri','Rahim','Stella',None,'Johnson'],
    'age': [34,40,None,None,28],
    'Salary' : [None,150,175,180,190],
    'City' :['Chennai','Mumbai',None,'Pune','Hyderabad']
}

df = pd.DataFrame(data)
print(df)

print(df.isnull())
print(df.isnull().sum())

df1 = df.dropna()
print(df1)
print(df1.isnull().sum())

print(df)

df2 = df.dropna(subset=['Salary'])
print(df2)


df2['age'] = df2['age'].fillna(df['age'].mean())
print(df2)


df2['age'] = df2['age'].fillna(18)
print(df2)

df2['name'] = df2['name'].fillna("UNKNOWN")
print(df2)

# Check         ->          isnull(), isna()
# Drop          ->          dropna()
# Fill miss     ->          fillna()
# Column-wise fill ->       df['age'/'city'/'col-name].fillnae(...)
# Fill          -> directvalue, mean()