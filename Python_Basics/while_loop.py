accuracy = 0.80
while accuracy < 0.96:
    accuracy += 0.03
    print(f"Training... current accuracy: {accuracy:.2f}")
