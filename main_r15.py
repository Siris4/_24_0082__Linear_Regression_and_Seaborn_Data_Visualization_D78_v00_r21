import pandas as pd

# Define the file path
file_path = r'C:\Users\Siris\Desktop\GitHub Projects 100 Days NewB\_24_0082__Day78_Linear_Regression_and_Seaborn_Data_Visualization__240826\NewProject\r00-r09 START\r00_env_START\cost_revenue_dirty.csv'

# Load the dataset
df = pd.read_csv(file_path)

# Define a function to clean the currency columns
def clean_currency(column):
    return column.replace({'\$': '', ',': ''}, regex=True).astype(int)

# Clean the USD_Worldwide_Gross column
df['USD_Worldwide_Gross'] = clean_currency(df['USD_Worldwide_Gross'])

# Count the number of films that grossed $0 worldwide
zero_worldwide_gross_count = (df['USD_Worldwide_Gross'] == 0).sum()

# Print the result
print(f"The number of films that grossed $0 worldwide is {zero_worldwide_gross_count}.")
