import numpy as np
# a = np.array([1, 2, 3])
# b = 5
# result = a + b  

# print("Result of broadcasting:", result)

# a = np.array([[1, 2, 3],
#               [4, 5, 6]])
# b = np.array([10, 20, 30])
# result = a + b
# print("Result of broadcasting:\n", result)

# a = np.array([[1, 2], [3, 4]])
# b = np.array([1, 2, 3])

# result = a + b  # This will raise an error due to incompatible shapes
# print("Result of broadcasting:\n", result)

# X = np.array([[10, 20, 30],
#               [40, 50, 60],
#               [70, 80, 90]])

# min_vals = X.min(axis=0)  # shape: (3,)
# max_vals = X.max(axis=0)  # shape: (3,)

# X_scaled = (X - min_vals) / (max_vals - min_vals)
# print("Scaled Data:\n", X_scaled)

# X = np.array([[1.2, 0.7],
#               [0.3, 0.5],
#               [0.9, 1.1]])

# bias = np.array([0.1])  # shape: (1,)
# X_with_bias = X + bias
# print("Data with Bias Term:\n", X_with_bias)

# def softmax(logits):
#     exp_vals = np.exp(logits - np.max(logits, axis=1, keepdims=True))
#     return exp_vals / np.sum(exp_vals, axis=1, keepdims=True)

# logits = np.array([[2.0, 1.0, 0.1],
#                    [1.0, 3.0, 0.2]])

# probs = softmax(logits)
# print("Softmax Probabilities:\n", probs)


X = np.array([[1, 2],
              [3, 4],
              [5, 6]])

query = np.array([2, 3])  # shape: (2,)
distances = np.sqrt(np.sum((X - query)**2, axis=1))
print("Distances from query point:", distances)