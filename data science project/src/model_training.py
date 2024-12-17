import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

def train_model(features, labels):
    """
    Trains a machine learning model using the provided features and labels.

    Parameters:
    features (DataFrame): The dataset containing engineered features.
    labels (Series): The target variable for model training.

    Returns:
    model: The trained machine learning model.
    accuracy: The accuracy of the model on the test set.
    report: A classification report of the model's performance.
    """
    
    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, random_state=42)
    
    # Initialize the Random Forest Classifier
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    
    # Fit the model on the training data
    model.fit(X_train, y_train)
    
    # Predict on the test data
    y_pred = model.predict(X_test)
    
    # Calculate the accuracy of the model
    accuracy = accuracy_score(y_test, y_pred)
    
    # Generate a classification report
    report = classification_report(y_test, y_pred)
    
    return model, accuracy, report