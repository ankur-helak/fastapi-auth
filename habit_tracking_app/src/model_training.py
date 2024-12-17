import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

def train_model(features, target):
    """
    Train a machine learning model using the provided features and target.

    Parameters:
    - features: DataFrame containing the engineered features.
    - target: Series or DataFrame containing the target variable.

    Returns:
    - model: Trained machine learning model.
    - accuracy: Accuracy score of the model on the test set.
    """

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

    # Initialize the RandomForestClassifier
    model = RandomForestClassifier(n_estimators=100, random_state=42)

    # Train the model
    model.fit(X_train, y_train)

    # Predict on the test set
    predictions = model.predict(X_test)

    # Calculate the accuracy
    accuracy = accuracy_score(y_test, predictions)

    return model, accuracy