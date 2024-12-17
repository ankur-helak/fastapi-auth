import pandas as pd
import numpy as np

def engineer_features(cleaned_data):
    """
    This function takes cleaned data as input and performs feature engineering tasks.
    It creates new features and transforms existing ones to enhance the predictive power of the dataset.
    
    Parameters:
    cleaned_data (DataFrame): The dataset after cleaning, ready for feature engineering.
    
    Returns:
    DataFrame: The dataset with engineered features.
    """
    
    # Example of creating a new feature: calculate the total amount spent
    if 'quantity' in cleaned_data.columns and 'price' in cleaned_data.columns:
        cleaned_data['total_spent'] = cleaned_data['quantity'] * cleaned_data['price']
    
    # Example of transforming an existing feature: log transformation to reduce skewness
    if 'total_spent' in cleaned_data.columns:
        cleaned_data['log_total_spent'] = np.log1p(cleaned_data['total_spent'])
    
    # Example of encoding categorical variables: one-hot encoding
    if 'category' in cleaned_data.columns:
        cleaned_data = pd.get_dummies(cleaned_data, columns=['category'], drop_first=True)
    
    # Example of feature scaling: standardization
    numeric_features = cleaned_data.select_dtypes(include=[np.number]).columns
    cleaned_data[numeric_features] = (cleaned_data[numeric_features] - cleaned_data[numeric_features].mean()) / cleaned_data[numeric_features].std()
    
    return cleaned_data