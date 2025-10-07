import pandas as pd

df = pd.DataFrame({
    'Age': [45, 50, 36],
    'BMI': [28.5, 31.2, 22.4],
    'Glucose': [130, 145, 110],
    'Outcome': [1, 1, 0]  # 1 = diabetic, 0 = non-diabetic
})
print("Data",df)
# - You can easily filter:

glucose_value = df[df['Glucose'] > 140]
print("Glucose > 140:\n", glucose_value)

# - Or engineer a new feature:

df['RiskScore'] = df['BMI'] * df['Glucose'] / df['Age']
print("With RiskScore:\n", df)
# - Or compute statistics:
mean_bmi = df['BMI'].mean()
print("Mean BMI:", mean_bmi)

