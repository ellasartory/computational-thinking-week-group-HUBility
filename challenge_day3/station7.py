def solution_station_7(expressions, known_vars):
    # Define the values of variables a, b, c, d, and e
    variables = {'a': 3, 'b': -1, 'c': 4, 'd': 7, 'e': 0.5}

    results = {}
    
    for expression in expressions:
        try:
            result = eval(expression, variables)
            results[expression] = result
        except Exception as e:
            print(f"Error evaluating {expression}: {e}")
            results[expression] = None

    return results

# Define the list of known variables
known_variables = ['a', 'b', 'c', 'd', 'e']

# Define the list of expressions to be evaluated
expressions = ['a * b + c', 'd - e', 'c / d']

# Calculate the values of expressions using the custom solver
results = solution_station_7(expressions, known_variables)

# Print the results
for expression, result in results.items():
    print(f"Result of {expression}: {result}")
