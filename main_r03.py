import pandas as pd

# Define the file path
file_path = r'C:\Users\Siris\Desktop\GitHub Projects 100 Days NewB\_24_0082__Day78_Linear_Regression_and_Seaborn_Data_Visualization__240826\NewProject\r00-r09 START\r00_env_START\cost_revenue_dirty.csv'

# Load the dataset
df = pd.read_csv(file_path)

# Check for duplicate rows
duplicates_exist = df.duplicated().any()

# Print the result
if duplicates_exist:
    print("The dataset contains duplicate rows.")
else:
    print("The dataset does not contain any duplicate rows.")
