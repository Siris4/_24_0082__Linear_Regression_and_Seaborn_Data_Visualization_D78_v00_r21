import pandas as pd

# Define the file path
file_path = r'C:\Users\Siris\Desktop\GitHub Projects 100 Days NewB\_24_0082__Day78_Linear_Regression_and_Seaborn_Data_Visualization__240826\NewProject\r00-r09 START\r00_env_START\cost_revenue_dirty.csv'

# Load the dataset
df = pd.read_csv(file_path)

# Define a function to clean the currency columns
def clean_currency(column):
    return column.replace({'\$': '', ',': ''}, regex=True).astype(float)

# Apply the function to the relevant columns
df['USD_Production_Budget'] = clean_currency(df['USD_Production_Budget'])
df['USD_Worldwide_Gross'] = clean_currency(df['USD_Worldwide_Gross'])
df['USD_Domestic_Gross'] = clean_currency(df['USD_Domestic_Gross'])

# Print the cleaned columns to verify
print(df[['USD_Production_Budget', 'USD_Worldwide_Gross', 'USD_Domestic_Gross']].head())

