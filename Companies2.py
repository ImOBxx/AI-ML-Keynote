import numpy as np 
import matplotlib.pyplot as plt 
  

years = np.array([2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024])
percentages = np.array([20, 47, 58, 50, 56, 50, 55, 72])

with plt.style.context('dark_background'): 
    plt.plot(years, percentages, 'r-o')  

  
    plt.xlabel("Year")
    plt.ylabel("Percentage")
    plt.title("Yearly Percentage Growth")


plt.show()
