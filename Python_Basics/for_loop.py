# for epoch in range(5):
#     print(f"Training epoch {epoch+1}...")

num_epochs = 5
def train_model():
    print("Model trained for one epoch.")

def evaluate_model():
    print("Model evaluated.")

for epoch in range(num_epochs):
    print(f"Epoch {epoch+1}/{num_epochs}")
    train_model()
    evaluate_model()
