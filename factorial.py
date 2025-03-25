def calculate_factorial(n):
    '''Calculate the factorial of a given number using a loop'''
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n+1):
        result *= i
    return result

def get_positive_integer():
    '''Get a positive integer from the user input with validation'''
    while True:
        try:
            num = int(input("Enter a positive integer to calculate its factorial: "))
            if num >= 0:
                return num
            else:
                print("Please enter a non-negative integer.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")