import pandas as pd

# Define the file path
file_path = r'C:\Users\Siris\Desktop\GitHub Projects 100 Days NewB\_24_0082__Day78_Linear_Regression_and_Seaborn_Data_Visualization__240826\NewProject\r00-r09 START\r00_env_START\cost_revenue_dirty.csv'

# Load the dataset
df = pd.read_csv(file_path)

# Define a function to clean the currency columns
def clean_currency(column):
    return column.replace({'\$': '', ',': ''}, regex=True).astype(int)

# Clean the USD_Production_Budget column
df['USD_Production_Budget'] = clean_currency(df['USD_Production_Budget'])

# Calculate the average production budget
average_production_budget = df['USD_Production_Budget'].mean()

# Print the result
print(f"The average production budget of the films is ${average_production_budget:.2f}")
