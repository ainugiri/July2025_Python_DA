import pandas as pd

df = pd.DataFrame(
    {
        'DAS_ID': ['A825825', 'A825826', 'A825827', 'A825828'],
        'Name': ['John', 'Jane', 'Doe', 'Smith'],
        'Age': [28, 34, 29, 40],
        'Salary': [50000, 60000, 55000, 70000],
        'Department': ['HR', 'Finance', 'IT', 'Marketing'],
        'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
    }
)
print(df)  # Print the DataFrame # tabular data structure with rows and columns

df1 = pd.read_csv('sample.csv')  # Read an Excel file into a DataFrame

print(df1)

# Sorting
print(df1.sort_values(by='name'))  # Sort by 'name' column


df2 = pd.read_csv('proj_details.csv')
print(df2)
print(df2.sort_values(by='des_level', ascending=False))  # Sort by 'proj_name' column

df3 = pd.merge(df1, df2, on='eid')  # Merge two DataFrames on 'eid' column
print(df3)  # Merge two DataFrames on 'eid' column

print(df3.columns)

df4 = pd.read_csv('Sample_A.csv')
df5 = pd.read_csv('proj_details_A.csv')
df6 = pd.merge(df4, df5, on='eid')
print(df6)  # Merge two DataFrames on 'eid' column

df6.to_csv('merged_output.csv', index=False)  # Save the merged DataFrame to a CSV file

df7 = pd.merge(df4,df5, on='eid', how='inner')
df7.to_csv('megerd_inner_op.csv',index=False)

df8 = pd.merge(df4,df5,on='eid', how='left')
df8.to_csv('merged_left_op.csv',index=False)

df9 = pd.merge(df4,df5,on='eid',how='right')
df9.to_csv('merged_right_op.csv',index=False)