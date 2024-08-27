import pandas as pd

# Define the file path
file_path = r'C:\Users\Siris\Desktop\GitHub Projects 100 Days NewB\_24_0082__Day78_Linear_Regression_and_Seaborn_Data_Visualization__240826\NewProject\r00-r09 START\r00_env_START\cost_revenue_dirty.csv'

# Load the dataset
df = pd.read_csv(file_path)

# Define a function to clean the currency columns
def clean_currency(column):
    return column.replace({'\$': '', ',': ''}, regex=True).astype(int)

# Clean the USD_Domestic_Gross column
df['USD_Domestic_Gross'] = clean_currency(df['USD_Domestic_Gross'])

# Count the number of films that grossed $0 domestically
zero_domestic_gross_count = (df['USD_Domestic_Gross'] == 0).sum()

# Print the result
print(f"The number of films that grossed $0 domestically is {zero_domestic_gross_count}.")
