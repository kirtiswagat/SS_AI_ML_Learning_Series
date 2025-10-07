import numpy as np
import matplotlib.pyplot as plt

data = [np.random.normal(0, std, 100) for std in range(1, 4)]
plt.boxplot(data, vert=True, patch_artist=True, 
            labels=["Low Var", "Med Var", "High Var"])
plt.title("Boxplots with Different Variances")
plt.ylabel("Value Distribution")
plt.show()