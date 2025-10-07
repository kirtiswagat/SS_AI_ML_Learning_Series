import numpy as np
import matplotlib.pyplot as plt
models = ["Model_A", "Model_B", "Model_C"]
train_acc = [0.85, 0.90, 0.88]
val_acc = [0.82, 0.87, 0.84]

x = np.arange(len(models))
width = 0.35

plt.bar(x - width/2, train_acc, width, label="Train Accuracy")
plt.bar(x + width/2, val_acc, width, label="Validation Accuracy")

plt.xticks(x, models)
plt.ylabel("Accuracy")
plt.title("Model Accuracy Comparison")
plt.legend()
plt.show()
