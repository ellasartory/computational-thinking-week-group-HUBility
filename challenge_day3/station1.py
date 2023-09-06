
#Fibonacci numbers sequence

def solution_station_1(n):
    if n <= 0:
        return []

    sequence = [0, 1]  # Initialize the sequence with the first two Fibonacci numbers

    if n <= 1:
        return sequence[:n + 1]

    a, b = 0, 1
    for _ in range(2, n + 1):
        next_fib = a + b
        sequence.append(next_fib)
        a, b = b, next_fib

    return sequence

