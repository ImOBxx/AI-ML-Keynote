import numpy as np 
import seaborn as sns 
import matplotlib.pyplot as plt

sectors = [
    "Accommodation and Food Services", "Agriculture, Forestry, and Fishing", 
    "Arts, Entertainment and Recreation", "Construction", "Education", 
    "Financial Services", "Healthcare", "Information and Communication", 
    "Manufacturing", "Other Services", "Professional Services", 
    "Public Services", "Social Services", "Transportation and Storage", 
    "Utilities", "Wholesale and Retail"
]

total_value = [
    1.5, 0.554, 0.453, 2.76, 1.06, 3.42, 2.26, 3.72, 
    8.4, 0.535, 7.47, 3.99, 1.08, 2.13, 0.962, 6.18
]

subset_value = [
    0.489, 0.215, 0.087, 0.52, 0.109, 1.15, 0.461, 0.951, 
    3.78, 0.095, 1.85, 0.939, 0.216, 0.744, 0.304, 2.23
]


sns.set_style("whitegrid")


plt.figure(figsize=(14, 10))
bars1 = plt.barh(sectors, total_value, color='b', alpha=0.7, label='Total Value')
bars2 = plt.barh(sectors, subset_value, color='orange', alpha=0.7, label='Subset Value')

plt.xlabel('Value (in trillions)', fontsize=14)
plt.title('Sector-wise Growth Total By AI Integration', fontsize=16)
plt.legend()


for bar in bars1:
    plt.text(bar.get_width() + 0.1, bar.get_y() + bar.get_height()/2, f'{bar.get_width():.2f}T', va='center', fontsize=10)

for bar in bars2:
    plt.text(bar.get_width() + 0.1, bar.get_y() + bar.get_height()/2, f'{bar.get_width():.2f}T', va='center', fontsize=10)

plt.grid(True, axis='x', linestyle='--', alpha=0.7)


plt.show()