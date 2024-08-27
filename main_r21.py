import pandas as pd

# Define the file path
file_path = r'C:\Users\Siris\Desktop\GitHub Projects 100 Days NewB\_24_0082__Day78_Linear_Regression_and_Seaborn_Data_Visualization__240826\NewProject\r00-r09 START\r00_env_START\cost_revenue_dirty.csv'

# Load the dataset
df = pd.read_csv(file_path)

# Define a function to clean the currency columns
def clean_currency(column):
    return column.replace({'\\$': '', ',': ''}, regex=True).astype(int)

# Clean the necessary columns
df['USD_Production_Budget'] = clean_currency(df['USD_Production_Budget'])
df['USD_Worldwide_Gross'] = clean_currency(df['USD_Worldwide_Gross'])

# Create a new DataFrame that excludes films not yet screened
cutoff_date = pd.to_datetime('2018-05-01')
df['Release_Date'] = pd.to_datetime(df['Release_Date'], errors='coerce')
data_clean = df.query('Release_Date <= @cutoff_date')

# Determine the number of films that did not break even
not_broken_even_count = data_clean.query('USD_Worldwide_Gross < USD_Production_Budget').shape[0]

# Calculate the total number of films in the data_clean DataFrame
total_films = data_clean.shape[0]

# Calculate the percentage of films that did not break even
percentage_not_broken_even = (not_broken_even_count / total_films) * 100

# Print the result
print(f"The percentage of films that did not break even at the box office is {percentage_not_broken_even:.2f}%.")
