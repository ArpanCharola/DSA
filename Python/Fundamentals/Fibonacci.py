# ---------------------------------------------------------------------------
# FIBONACCI NUMBER
# ---------------------------------------------------------------------------
# Problem:
#   Given an integer n, return the nth Fibonacci number.
#   The sequence is defined as:
#       F(0) = 0
#       F(1) = 1
#       F(n) = F(n - 1) + F(n - 2)   for n > 1
#
# Examples:
#   fib(2)  ->  1      (0, 1, 1)
#   fib(5)  ->  5      (0, 1, 1, 2, 3, 5)
#   fib(10) ->  55
#
# Constraints:
#   0 <= n <= 30   (keep it small so the recursive version still finishes)
#
# STRETCH GOAL: solve it TWO ways and print both results
#   1) Recursive  -> directly from the definition above
#   2) Iterative  -> with a loop and two running variables
#   Then notice: the recursive one gets painfully slow as n grows. Ask yourself why.
#
# Concept this builds: recursion vs iteration, and your first taste of time
# complexity (recursive ~ O(2^n)  vs  iterative ~ O(n)).
# ---------------------------------------------------------------------------

# Write your solution below 👇

#1. Recursive solution
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

#2. Iterative solution
def fibonacci_iterative(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a , b = b, a + b
        return b

def main():
    n = 35  # Example input
    print(f"Recursive Fibonacci of {n}: {fibonacci(n)}")
    print(f"Iterative Fibonacci of {n}: {fibonacci_iterative(n)}")

if __name__ == "__main__":
    main()