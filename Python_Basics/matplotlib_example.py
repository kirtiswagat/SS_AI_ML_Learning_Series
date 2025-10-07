import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# plt.plot(x, y)
# plt.title("Simple Line Plot")
# plt.xlabel("X-axis")
# plt.ylabel("Y-axis")
# plt.show()

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
plt.plot(x, y, color="green", marker="o", linestyle="--")
plt.title("Customized Line Plot")
plt.xlabel("Feature X")
plt.ylabel("Feature Y")
plt.grid(True)
plt.show()
