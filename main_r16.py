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
df['USD_Domestic_Gross'] = clean_currency(df['USD_Domestic_Gross'])

# Calculate the international gross revenue
df['USD_International_Gross'] = df['USD_Worldwide_Gross'] - df['USD_Domestic_Gross']

# Filter films that had $0 international gross revenue
zero_international_gross_films = df[df['USD_International_Gross'] == 0]

# Sort these films by production budget in descending order
highest_budget_zero_international_gross = zero_international_gross_films.sort_values(by='USD_Production_Budget', ascending=False)

# Print the top results with the movie names
print("The highest budget films that had no revenue internationally:")
print(highest_budget_zero_international_gross[['Movie_Title', 'USD_Production_Budget', 'USD_Worldwide_Gross', 'USD_Domestic_Gross', 'USD_International_Gross']])
