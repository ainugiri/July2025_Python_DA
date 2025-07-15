# scatter plot - relationship between two numerical variables
# Line plot - trends over time or ordered categories / sequence
# Bar plot - Average value comparison /comparison of categorical data
# Count plot - count of occurrences of categorical data / Frequency of categorical data
# Box plot - visualizes the distribution of a numerical variable across different categories
# Violin plot - combines box plot and density plot to show distribution
# Density plot - visualizes the distribution of a numerical variable
# Heatmap - visualizes the relationship between two numerical variables using color intensity
# Categorical plot - visualizes the distribution of a categorical variable
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve','Giri'],
    'Age': [24, 30, 22, 35, 29,25],
    'Salary': [50000, 60000, 55000, 70000, 65000,62000],
    'Department': ['HR', 'Finance', 'IT', 'Marketing', 'Sales','IT']
}

df = pd.DataFrame(data)
print(df)

# sns.lineplot(x='Age', y='Salary', data=df, marker='o')
# sns.scatterplot(x='Age', y='Salary', data=df, marker='o')
# sns.boxplot(x='Department', y='Salary', data=df)
# sns.violinplot(x='Department', y='Salary', data=df, inner='quartile')
# sns.swarmplot(x='Department', y='Salary', data=df, palette='Set2')
# sns.barplot(x='Name', y='Salary', data=df, palette='viridis')
# sns.pointplot(x='Name', y='Salary', data=df)
# sns.countplot(x='Department', data=df, palette='Set2')

# plt.title("Count of Employees by Department")
# plt.show()

iris_data = sns.load_dataset("iris")
print("Iris dataset loaded successfully.")
print("First few rows of the Iris dataset:")
print(iris_data.head())

# iris - flower dataset
# categorical variable - species
# numerical variables - sepal_length, sepal_width, petal_length, petal_width
# categories = setosa, versicolor, virginica
# setosa - is a species of iris flower - usully has smaller petals and sepals
# versicolor - is a species of iris flower - has medium sized petals and sepals
# virginica - is a species of iris flower - has larger petals and sepals


# sns.violinplot(x='species', y='petal_length', data=iris_data)
sns.scatterplot(x='sepal_length', y='sepal_width', hue='species', data=iris_data)
plt.title("Scatter Plot of Sepal Length vs Sepal Width by Species")
plt.show()
