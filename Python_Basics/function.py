# def greet_user(name):
#     print(f"Hello, {name}! Welcome to Python for AI/ML.")

# greet_user("Kirti Swagat")


# def calculate_accuracy(correct, total):
#     """Compute model accuracy percentage."""
#     return (correct / total) * 100

# accuracy = calculate_accuracy(85, 100)
# print(f"Accuracy: {accuracy:.2f}%")


# def train_model(epochs=10, learning_rate=0.001):
#     print(f"Training model for {epochs} epochs with LR={learning_rate}")

# train_model()
# train_model(epochs=20)
# train_model(learning_rate=0.005)

names = ['John', 'Alice', 'Bob']
scores = [85, 90, 78]
result = zip(names, scores)
print(list(result))

# def evaluate_accuracy(predictions, labels):
#     correct = sum(p == l for p, l in zip(predictions, labels))
#     return correct / len(labels)

# preds = [1, 0, 1, 1]
# actual = [1, 0, 0, 1]
# print("Accuracy:", evaluate_accuracy(preds, actual))


# def apply_activation(fn, x):
#     return fn(x)

# import math
# result = apply_activation(math.tanh, 0.8)

# print("Result after applying activation:", result)