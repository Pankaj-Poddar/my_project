def fibonacci(n):
    """Return the first n numbers in the Fibonacci series using recursion."""
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    def fib_helper(num):
        if num == 0:
            return 0
        elif num == 1:
            return 1
        else:
            return fib_helper(num - 1) + fib_helper(num - 2)
    
    return [fib_helper(i) for i in range(n)]


# Example usage
if __name__ == "__main__":
    print(fibonacci(10))  # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]