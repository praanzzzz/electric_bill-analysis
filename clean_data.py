import pandas as pd

# Step 1: Read the CSV file into a pandas DataFrame
file_path = 'eb.csv'
df = pd.read_csv(file_path)

# Step 2: Handle missing data
# Replace empty values in 'System Loss Charge' column with NaN
df['System Loss Charge'] = df['System Loss Charge'].replace('', pd.NA)

# Step 3: Convert data types
# Convert 'kwh_used' and 'System Loss Charge' columns to numeric, coercing errors to NaN
df['kwh_used'] = pd.to_numeric(df['kwh_used'], errors='coerce')
df['System Loss Charge'] = pd.to_numeric(df['System Loss Charge'], errors='coerce')

# Step 4: Save cleaned data to a new CSV file
cleaned_file_path = 'cleaned_electric_bill_data.csv'
df.to_csv(cleaned_file_path, index=False)

print(f"Cleaned data saved to {cleaned_file_path}")
