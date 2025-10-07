# import numpy as np
# import matplotlib.pyplot as plt

# categories = ["A", "B", "C", "D"]
# values = [23, 45, 56, 78]

# plt.bar(categories, values, color="teal")
# plt.title("Category Frequency")
# plt.xlabel("Category")
# plt.ylabel("Value")
# plt.show()

import numpy as np
import matplotlib.pyplot as plt

categories = ["A", "B", "C", "D"]
values = [23, 45, 56, 78]

plt.barh(categories, values, color=["#6A5ACD", 
                                    "#FF6347", 
                                    "#32CD32",
                                    "#FFD700"])
plt.title("Feature Comparison (Horizontal)")
plt.xlabel("Value")
plt.ylabel("Category")
plt.show()