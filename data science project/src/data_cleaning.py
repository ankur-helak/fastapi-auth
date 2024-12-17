import pandas as pd

def clean_data(data):
    """
    Cleans the input data by handling missing values, removing duplicates, and correcting data types.
    
    Parameters:
    data (DataFrame): The raw data to be cleaned.
    
    Returns:
    DataFrame: The cleaned data.
    """
    # Handle missing values by filling them with the mean of the column
    data.fillna(data.mean(), inplace=True)
    
    # Remove duplicate rows
    data.drop_duplicates(inplace=True)
    
    # Correct data types if necessary (example: converting object types to numeric)
    for column in data.select_dtypes(include=['object']).columns:
        try:
            data[column] = pd.to_numeric(data[column])
        except ValueError:
            # If conversion fails, leave the column as is
            pass
    
    return data

# Example usage
# raw_data = pd.read_csv('path_to_your_data.csv')
# cleaned_data = clean_data(raw_data)