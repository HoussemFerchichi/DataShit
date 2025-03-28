import numpy as np
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

def histogram(data, attribute):
    # Step 1: Aggregate counts for each attribute level
    attribute_values = {}
    for entry in data:
        key = entry[attribute]
        if key not in attribute_values:
            attribute_values[key] = 0
        attribute_values[key] += 1
    
    keys = list(attribute_values.keys())
    is_numerical = all(isinstance(k, (int, float)) for k in keys)
    
    if is_numerical:
        max_value = max(keys)
        bins = np.linspace(0, max_value, 11)
        counts = [0] * 10
        
        for key, count in attribute_values.items():
            for i in range(10):
                if bins[i] <= key < bins[i + 1]:
                    counts[i] += count
                    break
        
        bin_labels = [f"{bins[i]:.1f}-{bins[i+1]:.1f}" for i in range(10)]
        
        plt.bar(bin_labels, counts, color='blue', alpha=0.7)
        plt.xlabel(attribute)
        plt.ylabel("Number of Students")
        plt.xticks(rotation=45)
        plt.title(f"Histogram of {attribute}")
        plt.show()
        
        return max_value
    else:
        sorted_keys = sort_keys(keys)
        counts = [attribute_values[key] for key in sorted_keys]
        
        plt.bar(sorted_keys, counts, color='blue', alpha=0.7)
        plt.xlabel(attribute)
        plt.ylabel("Number of Students")
        plt.xticks(rotation=45)
        plt.title(f"Histogram of {attribute}")
        plt.show()
        
        return -1