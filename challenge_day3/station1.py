
#Fibonacci numbers
def solution_station_1(n):
 
    # Check if input is 0 
    if n < 0:
        print("Input not possible")
 
    # Check if n is 0
    elif n == 0:
        return 0
 
    # Check if n is 1,2
    elif n == 1 or n == 2:
        return 1
 
    else:
        return solution_station_1(n-1) + solution_station_1(n-2)
 
 
