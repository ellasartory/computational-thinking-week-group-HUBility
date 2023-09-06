def solution_station_7(expression, variables):
    try:
        result = eval(expression, variables)
        return result
    except Exception as e:
        print(f"Error: {e}")
        return None

# Define the values of variables a, b, c, d, and e
variables = {'a': 3, 'b': -1, 'c': 4, 'd': 7, 'e': 0.5}

