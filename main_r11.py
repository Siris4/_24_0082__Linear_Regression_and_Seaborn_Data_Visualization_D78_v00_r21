import pandas as pd

# Define the file path
file_path = r'C:\Users\Siris\Desktop\GitHub Projects 100 Days NewB\_24_0082__Day78_Linear_Regression_and_Seaborn_Data_Visualization__240826\NewProject\r00-r09 START\r00_env_START\cost_revenue_dirty.csv'

# Load the dataset
df = pd.read_csv(file_path)

# Define a function to clean the currency columns
def clean_currency(column):
    return column.replace({'\$': '', ',': ''}, regex=True).astype(int)

# Clean the necessary columns
df['USD_Production_Budget'] = clean_currency(df['USD_Production_Budget'])
df['USD_Worldwide_Gross'] = clean_currency(df['USD_Worldwide_Gross'])

# Find the highest production budget
max_production_budget = df['USD_Production_Budget'].max()

# Find the highest worldwide gross revenue
max_worldwide_gross = df['USD_Worldwide_Gross'].max()

# Print the results
print(f"The highest production budget of any film is ${max_production_budget}.")
print(f"The highest worldwide gross revenue of any film is ${max_worldwide_gross}.")
