def fibonacci (n):
    #First two Fibonacci numbers
    fib_sequence = [0, 1]
    
    #Generate the Fibonacci sequence up to n-th term
    for i in range(2, n):
        fib_sequence.append(fib_sequence[i-1] + fib_sequence[i-2])
    return fib_sequence[ : n]
#Input the number of terms to print
n = int(input("Enter the number of terms: "))
#Output the Fibonacci sequence up to n-th term
print(fibonacci(n))
