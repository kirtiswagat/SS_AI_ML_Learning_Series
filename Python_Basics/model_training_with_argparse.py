import argparse
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from joblib import dump

def train_model(data_path, target_column, n_estimators, output_model):
    # Load dataset
    df = pd.read_csv(data_path)
    X = df.drop(columns=[target_column])
    y = df[target_column]

    # Train model
    model = RandomForestClassifier(n_estimators=n_estimators, random_state=42)
    model.fit(X, y)

    # Evaluate
    preds = model.predict(X)
    acc = accuracy_score(y, preds)
    print(f"Training Accuracy: {acc:.4f}")

    # Save model
    dump(model, output_model)
    print(f"Model saved to {output_model}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Train a Random Forest model on tabular data.")
    parser.add_argument("--data_path", type=str, required=True, help="Path to CSV dataset")
    parser.add_argument("--target_column", type=str, required=True, help="Name of target column")
    parser.add_argument("--n_estimators", type=int, default=100, help="Number of trees in the forest")
    parser.add_argument("--output_model", type=str, default="model.joblib", help="Path to save trained model")

    args = parser.parse_args()
    train_model(args.data_path, args.target_column, args.n_estimators, args.output_model)