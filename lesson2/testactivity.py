import numpy as np
from activity2 import data

# Import data from activity2.py

def calculate_line_of_best_fit(x_data, y_data):
    """
    Calculate the line of best fit using least squares method.
    Returns gradient (slope) and y-intercept.
    """
    # Convert to numpy arrays if needed
    x = np.array(x_data)
    y = np.array(y_data)
    
    # Calculate gradient and y-intercept using least squares
    gradient = (len(x) * np.sum(x * y) - np.sum(x) * np.sum(y)) / \
               (len(x) * np.sum(x**2) - np.sum(x)**2)
    
    y_intercept = (np.sum(y) - gradient * np.sum(x)) / len(x)
    
    return gradient, y_intercept

# Main execution
if __name__ == "__main__":
    # Assuming data from activity2.py is in format: x_values, y_values
    x_values = data[0]  # Adjust indexing based on your activity2.py structure
    y_values = data[1]
    
    gradient, y_intercept = calculate_line_of_best_fit(x_values, y_values)
    
    print(f"Gradient (slope): {gradient:.4f}")
    print(f"Y-intercept: {y_intercept:.4f}")
    print(f"Equation: y = {gradient:.4f}x + {y_intercept:.4f}")