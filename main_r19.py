import pandas as pd

# Define the file path
file_path = r'C:\Users\Siris\Desktop\GitHub Projects 100 Days NewB\_24_0082__Day78_Linear_Regression_and_Seaborn_Data_Visualization__240826\NewProject\r00-r09 START\r00_env_START\cost_revenue_dirty.csv'

# Load the dataset
df = pd.read_csv(file_path)

# Convert the Release_Date column to datetime format
df['Release_Date'] = pd.to_datetime(df['Release_Date'], errors='coerce')

# Define the cutoff date
cutoff_date = pd.to_datetime('2018-05-01')

# Identify films that were not released yet as of the cutoff date
unreleased_films = df.query('Release_Date > @cutoff_date')

# Count the number of films that have not yet had a chance to be screened
unreleased_films_count = unreleased_films.shape[0]

# Print the result
print(f"The number of films that have not yet had a chance to be screened in the box office as of May 1st, 2018 is {unreleased_films_count}.")
