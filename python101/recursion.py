
# def fib(n):
#     if n == 1:  # Base case
#         return 1
#     else:
#        fib

# print(fib(5))



def fibonacci_recursive(n):
    # Handle base cases
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]

    # Recursive call to get the Fibonacci sequence
    fib_sequence = fibonacci_recursive(n - 1)
    fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])

    return fib_sequence

# Example usage:
n = 10
fib_sequence = fibonacci_recursive(n)
print(f"The Fibonacci sequence up to {n} terms: {fib_sequence}")




