# Import necessary libraries
import pandas as pd
import numpy as np

def engineer_features(cleaned_data):
    """
    This function takes cleaned data as input and returns data with engineered features.
    
    Parameters:
    cleaned_data (DataFrame): A pandas DataFrame containing cleaned data.

    Returns:
    DataFrame: A pandas DataFrame with new and transformed features.
    """
    
    # Example feature engineering steps:
    
    # 1. Create new features based on existing ones
    # Assuming 'cleaned_data' has columns 'feature1' and 'feature2'
    cleaned_data['feature_sum'] = cleaned_data['feature1'] + cleaned_data['feature2']
    cleaned_data['feature_diff'] = cleaned_data['feature1'] - cleaned_data['feature2']
    
    # 2. Transform features
    # Log transformation to reduce skewness
    cleaned_data['log_feature1'] = np.log1p(cleaned_data['feature1'])
    
    # 3. Encoding categorical variables
    # Assuming 'cleaned_data' has a categorical column 'category_feature'
    cleaned_data = pd.get_dummies(cleaned_data, columns=['category_feature'], drop_first=True)
    
    # Return the DataFrame with engineered features
    return cleaned_data

# Export the engineer_features function
__all__ = ['engineer_features']