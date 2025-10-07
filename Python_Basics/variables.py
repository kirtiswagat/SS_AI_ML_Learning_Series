# Variables and basic types
project_name = "AI Forecast"
year = 2025
accuracy_score = 98.5
is_production_ready = True

# Lists (Mutable, Ordered)
models = ['Regression', 'SVM', 'CNN']
models.append('RNN') # ['Regression', 'SVM', 'CNN', 'RNN']
first_model = models[0] # 'Regression'

# Dictionaries (Mutable, Key-Value pairs)
hyperparameters = {
    'learning_rate': 0.01,
    'epochs': 100,
    'optimizer': 'Adam'
}
print("Models:", models)
print(f"Learning Rate: {hyperparameters['learning_rate']}")