import numpy as np
from scipy.optimize import root

def solution_station_7(expressions, known_vars):
    def equations_to_solve(x):
        return [
            x[0] + x[1] + x[2] + x[3] - 13,
            x[3] * x[2] - 28,
            x[3] * x[0] + x[2] * x[1] - 17,
            x[3] * x[0] * x[2] * x[4] - 42,
            x[4] + x[3] + x[1] * x[2] - 3.5
        ]

    # Initialize the initial guess for the unknowns
    initial_guess = np.array([1.0, 1.0, 1.0, 1.0, 1.0])

    # Use a numerical solver to find the values of the unknowns
    solution = root(equations_to_solve, initial_guess)

    return solution.x

# Define the list of known variables
known_variables = ['a', 'b', 'c', 'd', 'e']

# Calculate the values of expressions using the custom solver
solution = solution_station_7([], known_variables)

# Print the values of the variables
for var, value in zip(known_variables, solution):
    print(f"{var} =", value)