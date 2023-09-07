a = 3
b = -1
c = 4
d = 7
e = 0.5

def solution_station_7(expression):
    try:
        result = eval(expression)
        result = float(result)
        return result
    except Exception as e:
        print(f"Error: {e}")
        return None
