import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read the data from CSV file
df = pd.read_csv('eb.csv')

# Set 'bill month' as the index
df.set_index('bill month', inplace=True)

# Bar Plot
plt.figure(figsize=(12, 8))
df.plot(kind='bar')
plt.title('Electric Bill Analysis (2024) - Bar Plot')
plt.xlabel('Month')
plt.ylabel('Value')
plt.xticks(rotation=45)
plt.grid(True)
plt.legend(loc='upper right')
plt.tight_layout()
plt.show()

# Box Plot
plt.figure(figsize=(12, 8))
df.plot(kind='box')
plt.title('Electric Bill Analysis (2024) - Box Plot')
plt.ylabel('Value')
plt.grid(True)
plt.tight_layout()
plt.show()

# Correlation Heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm', vmin=-1, vmax=1)
plt.title('Correlation Heatmap of Electric Bill Variables')
plt.tight_layout()
plt.show()

# Pairplot
sns.pairplot(df)
plt.suptitle('Pairplot of Electric Bill Variables', y=1.02)
plt.show()
