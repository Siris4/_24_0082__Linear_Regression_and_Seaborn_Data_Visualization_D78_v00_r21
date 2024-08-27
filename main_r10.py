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

# Calculate the 25th percentile (bottom 25%)
percentile_25 = df['USD_Worldwide_Gross'].quantile(0.25)

# Filter the bottom 25% of films
bottom_25_films = df[df['USD_Worldwide_Gross'] <= percentile_25]

# Determine profitability: True if Worldwide Gross > Production Budget
bottom_25_films['Profitable'] = bottom_25_films['USD_Worldwide_Gross'] > bottom_25_films['USD_Production_Budget']

# Count how many are profitable and how many are not
profitable_count = bottom_25_films['Profitable'].sum()
unprofitable_count = len(bottom_25_films) - profitable_count

# Print the results
print(f"Out of the bottom 25% of films, {profitable_count} are profitable and {unprofitable_count} lose money.")
