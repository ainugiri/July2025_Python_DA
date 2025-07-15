import seaborn as sns
import matplotlib.pyplot as plt
print("Seaborn version:", sns.__version__)
print("Dataset available:", sns.get_dataset_names())

data = sns.load_dataset("tips")
print("First few rows of the dataset:")
print(data.head())

sns.scatterplot(x="total_bill", y="tip", data=data)
plt.title("Scatter plot of Total Bill vs Tip")
plt.xlabel("Total Bill ($)")
plt.ylabel("Tip ($)")
plt.show()

sns.lineplot(x="size", y="total_bill", data=data, marker="o")
plt.title("Line plot of Size vs Total Bill")
plt.xlabel("Size of Party")
plt.ylabel("Total Bill ($)")
plt.show()

sns.barplot(x="day", y="total_bill", data=data, palette="viridis")
plt.title("Bar plot of Total Bill by Day")
plt.xlabel("Day of the Week")
plt.ylabel("Total Bill ($)")
plt.show()


sns.countplot(x='day', data=data)
plt.title("Number of Bill by Day")
plt.show()

sns.boxplot(x="day", y="total_bill", data=data)
plt.title("Box plot of Total Bill by Day")  
plt.xlabel("Day of the Week")
plt.ylabel("Total Bill ($)")
plt.show()

# desinty plot
# visualizes the distribution of a numerical variable
sns.kdeplot(data['total_bill'], shade=True)
plt.title("Density Plot of Total Bill")
plt.xlabel("Total Bill ($)")
plt.ylabel("Density")
plt.show()

# violin plot
# x axis is categorical, y axis is numerical
# visualizes the distribution of the data
# combines the benefits of box plots and density plots

sns.violinplot(x="day", y="total_bill", data=data, inner="quartile")
plt.title("Violin Plot of Total Bill by Day")
plt.xlabel("Day of the Week")
plt.ylabel("Total Bill ($)")
plt.show()


# histogram - visualizes the distribution of a numerical variable
sns.histplot(data['total_bill'],kde=True)
plt.title("Histogram of Total Bill")
plt.xlabel("Total Bill ($)")
plt.ylabel("Frequency")
plt.show()


# catergorical plot - visualizes the distribution of a categorical variable
sns.catplot(x="day", y="total_bill", kind="bar", data=data, palette="coolwarm")
plt.title("Categorical Plot of Total Bill by Day")
plt.xlabel("Day of the Week")
plt.ylabel("Total Bill ($)")
plt.show()


# pairplot - visualizes the pairwise relationships in a dataset
sns.pairplot(data,hue='sex')
plt.title("Pairplot of Tips Dataset")
plt.show()

# hue - categorical variable, here it is used to color the points based on the 'sex' variable.
#  if it male the points will be blue, 
#  if female the points will be orange.

sns.set_style("whitegrid")
sns.set_palette("pastel")
sns.boxplot(x="day", y="tip", data=data)
plt.title("Box Plot of Tips by Day")
plt.xlabel("Day of the Week")
plt.ylabel("Tips ($)")
plt.show()

# Heatmap - visualizes the correlation between numerical variables


correlation_matrix = data.corr(numeric_only=True)
print("Correlation matrix:")
print(correlation_matrix)
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Heatmap of Correlation Matrix")
plt.show()