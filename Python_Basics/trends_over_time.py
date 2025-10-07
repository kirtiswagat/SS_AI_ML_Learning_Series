import pandas as pd
import matplotlib.pyplot as plt

# Sample trend data
data = {
        "Month": ["Jan", "Feb", "Mar", "Apr", "May"], 
        "Sales": [200, 300, 400, 350, 500]
        }
df = pd.DataFrame(data)

print("Data:\n",df)
plt.plot(df["Month"], df["Sales"], marker="o")
plt.title("Sales Trend Over Time")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()
