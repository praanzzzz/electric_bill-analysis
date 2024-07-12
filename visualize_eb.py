import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Read the cleaned CSV file into a pandas DataFrame
cleaned_file_path = 'cleaned_electric_bill_data.csv'
eb = 'eb.csv'
df = pd.read_csv(eb)

# Step 2: Calculate the Generation Charge (GC)
df['Generation Charge'] = df['kwh_used'] * df['rate/kwh']

# Step 3: Create the Matplotlib plot for 'rate/kwh', 'kwh_used', 'System Loss Charge', and 'Generation Charge'
plt.figure(figsize=(12, 6))

# Plot 'rate/kwh'
plt.plot(df['bill date'], df['rate/kwh'], marker='o', label='Rate/kWh')

# Plot 'kwh_used'
plt.plot(df['bill date'], df['kwh_used'], marker='s', label='kWh Used')

# Plot 'System Loss Charge'
plt.plot(df['bill date'], df['System Loss Charge'], marker='^', label='System Loss Charge')

# Plot 'Generation Charge'
plt.plot(df['bill date'], df['Generation Charge'], marker='d', label='Generation Charge')

# Add labels and title
plt.xlabel('Bill Date')
plt.ylabel('Amount')
plt.title('Electric Bill Components')
plt.legend()

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)

# Show plot
plt.tight_layout()
plt.grid(True)
plt.show()
