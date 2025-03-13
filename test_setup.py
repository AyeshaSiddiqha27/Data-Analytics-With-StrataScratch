# Import necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Create a sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emma'],
    'Age': [25, 30, 35, 40, 28],
    'Salary': [50000, 60000, 75000, 80000, 55000]
}
df = pd.DataFrame(data)

# Display DataFrame
print("\nSample DataFrame:")
print(df)

# Plot data using Seaborn (Assign 'x' to 'hue' and disable legend)
sns.set(style="whitegrid")
plt.figure(figsize=(8, 5))
sns.barplot(x='Name', y='Salary', data=df, hue='Name', palette='viridis', legend=False)

# Customize plot
plt.title('Sample Salary Data')
plt.xlabel('Employee Name')
plt.ylabel('Salary')

# Show plot
plt.show()
