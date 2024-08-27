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
df['USD_Domestic_Gross'] = clean_currency(df['USD_Domestic_Gross'])

# Filter films that grossed $0 domestically
zero_domestic_gross_films = df[df['USD_Domestic_Gross'] == 0]

# Sort these films by production budget in descending order and get the top 5
top_5_highest_budget_zero_gross = zero_domestic_gross_films.sort_values(by='USD_Production_Budget', ascending=False).head(5)

# Print the result with the movie names
print("The top 5 highest budget films that grossed nothing domestically:")
print(top_5_highest_budget_zero_gross[['Movie_Title', 'USD_Production_Budget', 'USD_Worldwide_Gross', 'USD_Domestic_Gross']])
