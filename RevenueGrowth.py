import matplotlib.pyplot as plt
import seaborn as sns


sns.set_style("darkgrid")



years = [2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025]
revenue = [10.1, 14.69, 22.59, 34.87, 51.27, 70.94, 94.41, 126]


plt.figure(figsize=(10, 6))
plt.plot(years, revenue, marker='o', linestyle='-', color='b')


plt.title('AI Revenue Growth (2018 - 2025)', fontsize=16)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Revenue (in billions)', fontsize=14)
plt.grid(True)


plt.show()
