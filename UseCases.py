import numpy as np
import matplotlib.pyplot as plt


use_cases = [
    "Customer intelligence",
    "Customer experience",
    "Retaining customers",
    "Interacting with customers",
    "Recommender systems",
    "Detecting fraud",
    "Reducing customer churn",
    "Acquiring customers",
    "Customer loyalty",
    "Customer engagement",
    "brand awareness",
    "Other"
]

data_2020 = [37, 34, 29, 28, 27, 27, 26, 26, 20, 19, 14, 15]
data_2021 = [50, 57, 31, 48, 27, 46, 22, 34, 40, 44, 31, 1]


x = np.arange(len(use_cases))
width = 0.35 

plt.figure(figsize=(8, 6))
bars1 = plt.barh(x - width/2, data_2020, width, label='2020', color='b')
bars2 = plt.barh(x + width/2, data_2021, width, label='2021', color='orange')


plt.xlabel('Percentage', fontsize=14)
plt.title('Use Case Comparison: AI Integration', fontsize=16)
plt.yticks(x, use_cases, fontsize=12)



for bar in bars1:
    plt.text(bar.get_width() + 0.5, bar.get_y() + bar.get_height()/2, f'{bar.get_width()}%', va='center', fontsize=10)

for bar in bars2:
    plt.text(bar.get_width() + 0.5, bar.get_y() + bar.get_height()/2, f'{bar.get_width()}%', va='center', fontsize=10)

plt.grid(True, axis='x', linestyle='--', alpha=0.7)

plt.show()
