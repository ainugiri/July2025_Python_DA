# from plotnine import geom_col, ggplot, aes, geom_point
# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
# iris_data = sns.load_dataset('iris')
# df = pd.DataFrame(iris_data)
# ggplot(df) + aes(x='species', y='sepal_length') + geom_col()
# # Display the plot
# plt.show()

from plotnine import geom_col, ggplot, aes, geom_point
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Giri'],
    'Age': [24, 30, 22, 35, 29, 25],
    'Salary': [50000, 60000, 55000, 70000, 65000, 62000],
    'Department': ['HR', 'Finance', 'IT', 'Marketing', 'Sales', 'IT']
}
df = pd.DataFrame(data)

ggplot(df) + aes(x='Name', y='Salary') + geom_col() 
plt.show()