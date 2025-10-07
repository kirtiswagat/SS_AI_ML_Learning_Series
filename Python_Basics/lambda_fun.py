models = [
    {'name': 'Model_A', 'accuracy': 0.91},
    {'name': 'Model_B', 'accuracy': 0.87},
    {'name': 'Model_C', 'accuracy': 0.94}
]

# Sort by accuracy
sorted_models = sorted(models, key=lambda m: m['accuracy'], reverse=True)
print("Sorted Models are:\n",sorted_models)

# 🔁 map() → Apply Transformation
# Use Case: Scaling features before model training
features = [120, 340, 560]
scaled = list(map(lambda x: x / 1000, features))
print("Scaled features are:\n",scaled)

# Used in pipelines to normalize input features for models like logistic regression or neural nets.

# 🚦 filter() → Filter Elements
# Use Case: Selecting high-confidence predictions
predictions = [0.95, 0.62, 0.88, 0.45]
confident = list(filter(lambda x: x > 0.80, predictions))
print("Confident predictions are:\n",confident)


# 📌 Useful in post-processing to retain only predictions above a threshold for downstream tasks.

# 📊 sorted() → Custom Sorting
# Use Case: Ranking models by validation accuracy
models = [('ModelA', 0.82), ('ModelB', 0.91), ('ModelC', 0.87)]
ranked = sorted(models, key=lambda x: x[1], reverse=True)
print("Ranked models are:\n",ranked)


# 📌 Helps in AutoML or ensemble selection by sorting based on performance metrics.

# 🧼 apply() (Pandas) → Feature Scaling / Cleaning
# Use Case: Column-wise normalization in a DataFrame
import pandas as pd

df = pd.DataFrame({'age': [25, 45, 35], 'income': [50000, 80000, 60000]})
df['income_scaled'] = df['income'].apply(lambda x: x / 1000)
print("DataFrame with scaled income:\n",df)
# 📌 Common in preprocessing steps for tabular ML models like XGBoost or LightGBM.




