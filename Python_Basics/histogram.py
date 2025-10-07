import numpy as np
import matplotlib.pyplot as plt

data = np.random.randn(1000)  # normally distributed
plt.hist(data, bins=30, color="skyblue", edgecolor="black")
plt.title("Normal Distribution of Data")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()
