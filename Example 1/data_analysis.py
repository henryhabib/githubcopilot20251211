import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

def clean_data(df):
    # Handle missing values
    df = df.dropna()  # Drop rows with missing values           
    
    return df

def split_data(df, column, bins):
    # Split the DataFrame into subsets based on bins of a specific column
    df['bin'] = pd.cut(df[column], bins=bins, labels=False)
    subsets = {f'bin_{i}': df[df['bin'] == i].drop(columns=['bin']) for i in range(len(bins) - 1)}
    return subsets

def perform_linear_regression(df, target_column):
    # Separate features and target
    X = df.drop(columns=[target_column])
    y = df[target_column]
    
    # Split into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Train the model
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    # Make predictions
    y_pred = model.predict(X_test)
    
    # Evaluate the model
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    
    return model, mse, r2

if __name__ == "__main__":
    # Example usage
    # Load your DataFrame (replace with your actual data source)
    df = pd.DataFrame({
        'feature1': np.random.rand(100) * 100,
        'feature2': np.random.rand(100) * 50,
        'target': np.random.rand(100) * 10
    })
    
    # Clean the data
    df = clean_data(df)
    
    # Split the data into subsets based on 'feature1'
    bins = [0, 25, 50, 75, 100]
    subsets = split_data(df, 'feature1', bins)
    
    # Perform linear regression on each subset
    for subset_name, subset_df in subsets.items():
        print(f"Processing {subset_name}...")
        if len(subset_df) > 1:  # Ensure there is enough data for regression
            model, mse, r2 = perform_linear_regression(subset_df, 'target')
            print(f"Model for {subset_name}: MSE={mse:.2f}, R2={r2:.2f}")
        else:
            print(f"Not enough data in {subset_name} for regression.")




