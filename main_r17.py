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

# Use the query function to filter for international releases with zero domestic gross and non-zero worldwide gross
international_releases = df.query('USD_Domestic_Gross == 0 and USD_Worldwide_Gross != 0')

# Print the number of international releases and display the top results
print(f'Number of international releases: {len(international_releases)}')
international_releases.head()
