from sympy import symbols, Eq, solve
import numpy as np

def solution_station_7(expressions, known_vars):
    def equations_to_solve(x):
        return [expression.subs({a: x[0], b: x[1], c: x[2], d: x[3], e: x[4]}) for expression in expressions]

    # Initialize the initial guess for the unknowns
    initial_guess = np.array([1.0, 1.0, 1.0, 1.0, 1.0])

    # Use a numerical solver to find the values of the unknowns
    solution = np.linalg.solve(np.array([equations_to_solve(initial_guess)]).T, [0.0])

    # Calculate expressions based on the known variables
    result_1 = solution[0] + initial_guess[1]
    result_2 = initial_guess[0] + initial_guess[2] * solution[0] + initial_guess[4]

    return solution

# Define the input equations (in terms of symbols a, b, c, d, e)
a, b, c, d, e = symbols('a b c d e')
equations = [
    a + b + c + d - 13,
    d * c - 28,
    d * a + c * b - 17,
    d * a * c * e - 42,
    e + d + b * c - 3.5
]

# Define the list of known variables
known_variables = [a, b, c, d, e]

# Calculate the values of expressions using the custom solver
solution = solution_station_7(equations, known_variables)

# Print the values of the variables
print("a =", solution[0])
print("b =", solution[1])
print("c =", solution[2])
print("d =", solution[3])
print("e =", solution[4])
