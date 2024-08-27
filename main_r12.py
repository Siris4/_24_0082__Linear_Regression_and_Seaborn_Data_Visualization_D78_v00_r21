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

# Find the lowest and highest budget films
lowest_budget_film = df.loc[df['USD_Production_Budget'].idxmin()]
highest_budget_film = df.loc[df['USD_Production_Budget'].idxmax()]

# Get the revenue for the lowest and highest budget films
lowest_budget_revenue = lowest_budget_film['USD_Worldwide_Gross']
highest_budget_revenue = highest_budget_film['USD_Worldwide_Gross']

# Print the results
print(f"The film with the lowest budget made ${lowest_budget_revenue} in worldwide gross revenue.")
print(f"The film with the highest budget made ${highest_budget_revenue} in worldwide gross revenue.")
