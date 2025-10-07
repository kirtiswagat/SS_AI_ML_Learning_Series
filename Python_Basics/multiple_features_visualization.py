import pandas as pd
import matplotlib.pyplot as plt
months = ["Jan", "Feb", "Mar", "Apr", "May"]
sales = [200, 300, 400, 350, 500]
profit = [50, 70, 80, 65, 100]

plt.plot(months, sales, label="Sales", marker="o")
plt.plot(months, profit, label="Profit", marker="s")
plt.title("Sales vs Profit Trend")
plt.xlabel("Month")
plt.ylabel("Value")
plt.legend()
plt.show()
