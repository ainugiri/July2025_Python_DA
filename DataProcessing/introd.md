Data processing 
convert the raw data -  structured data

If i want process data, we need data
load the data
data = load_data('path/to/data')
read data
data = read_data(data)

# Data Processing Introduction
check info
-> no of data, rows, columns
check_info(data)

# Statistical analysis
mean, median, mode

convert the raw into structured data (DataFrame)
df.describe()


# outliers 

if your data has outliers, you can remove them
def remove_outliers(data):
    # Implement outlier removal logic
    pass

    then most of the data are cleaned, structured.



load 
convert into df
process data
outliers
remove outliers
