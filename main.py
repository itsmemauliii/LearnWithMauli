import numpy as np

def calculate(input_list):
    # Check if the input list has exactly 9 elements
    if len(input_list) != 9:
        raise ValueError("List must contain nine numbers.")

    # Convert the input list into a 3x3 NumPy array
    matrix = np.array(input_list).reshape(3, 3)

    # Calculate the necessary statistics
    calculations =  {
        'mean': [matrix.mean(axis=0).tolist(), matrix.mean(axis=1).tolist(), matrix.mean().tolist()],
        'variance': [matrix.var(axis=0).tolist(), matrix.var(axis=1).tolist(), matrix.var().tolist()],
        'standard deviation': [matrix.std(axis=0).tolist(), matrix.std(axis=1).tolist(), matrix.std().tolist()],
        'max': [matrix.max(axis=0).tolist(), matrix.max(axis=1).tolist(), matrix.max().tolist()],
        'min': [matrix.min(axis=0).tolist(), matrix.min(axis=1).tolist(), matrix.min().tolist()],
        'sum': [matrix.sum(axis=0).tolist(), matrix.sum(axis=1).tolist(), matrix.sum().tolist()]
    }

    return calculations

# Now let's test our function
if __name__ == "__main__":
    # input for an instance
    input_list = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    try:
        result = calculate(input_list)
        print(result)
    except ValueError as e:
        print(e)
