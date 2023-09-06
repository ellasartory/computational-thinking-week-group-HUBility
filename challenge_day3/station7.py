def solution_station_7(expression):
    # Define the values of variables a, b, c, d, and e
    variables = {'a': 3, 'b': -1, 'c': 4, 'd': 7, 'e': 0.5}

    try:
        result = eval(expression, variables)
        return result
    except Exception as e:
        print(f"Error: {e}")
        return None


