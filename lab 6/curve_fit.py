import numpy as np
import numpy.polynomial.polynomial as poly
import matplotlib.pyplot as plt

def sort_keys(keys):
    # Implementing a simple sorting function (Insertion Sort)
    for i in range(1, len(keys)):
        key = keys[i]
        j = i - 1
        while j >= 0 and keys[j] > key:
            keys[j + 1] = keys[j]
            j -= 1
        keys[j + 1] = key
    return keys

def curve_fit(data, attribute, degree):
    # Step 1: Aggregate AvgGrade values for each unique attribute level
    attribute_values = {}
    for entry in data:
        key = entry[attribute]
        if key not in attribute_values:
            attribute_values[key] = []
        attribute_values[key].append(entry["AvgGrade"])
    
    # Step 2: Compute the average AvgGrade for each attribute level
    x_vals = list(attribute_values.keys())
    x_vals = sort_keys(x_vals)  # Using custom sorting function
    y_vals = [np.mean(attribute_values[key]) for key in x_vals]
    
    # Step 3: Determine if regression or interpolation is needed
    n_points = len(x_vals)
    if degree >= n_points:
        degree = n_points - 1  # Use interpolation instead of regression
    
    # Step 4: Fit the polynomial
    coefficients = np.polyfit(x_vals, y_vals, degree)
    polynomial = np.poly1d(coefficients)
    
    # Step 5: Plot the data and the fitted curve
    x_range = np.linspace(min(x_vals), max(x_vals), 100)
    y_range = polynomial(x_range)
    
    plt.scatter(x_vals, y_vals, color='red', label='Data Points')
    plt.plot(x_range, y_range, color='blue', label=f'Polynomial Fit (degree {degree})')
    plt.xlabel(attribute)
    plt.ylabel("AvgGrade")
    plt.legend()
    plt.show()
    
    # Step 6: Construct the polynomial equation as a string
    equation_terms = []
    num_coeffs = len(coefficients)
    for i in range(num_coeffs):
        coef = coefficients[num_coeffs - 1 - i]
        if i == 0:
            term = f"{coef:.4f}"
        elif i == 1:
            term = f"{coef:.4f}x"
        else:
            term = f"{coef:.4f}x^{i}"
        equation_terms.append(term)
    
    return "y = " + " + ".join(equation_terms)
print(curve_fit())