# Summarize - Group - Aggregation on Data
import pandas as pd


data = {
    'Region' : ['N','N','E','N','S','S','S','W','W','N'],
    'Products' : ['A','A','A','A','B','B','B','B','A','A'],
    'Sales' : [100,75,85,95,100,75,85,95,100,75],
    'Qty' : [10,8,7,10,9,7,2,3,10,11]
}


df = pd.DataFrame(data)
print(df)

print(pd.pivot_table(df, index='Region',values='Qty',aggfunc='sum'))

print(pd.pivot_table(df, index='Region',values=['Qty', 'Sales'],aggfunc='sum'))

print(pd.pivot_table(df, index='Region',values=['Qty', 'Sales'],aggfunc='mean'))

df5 = pd.pivot_table(df, index='Region',columns='Products',values=['Qty', 'Sales'],aggfunc='sum')
df5.to_excel('Sample.xlsx')
