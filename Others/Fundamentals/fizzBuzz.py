# ---------------------------------------------------------------------------
# FIZZBUZZ   (LeetCode 412)
# ---------------------------------------------------------------------------
# Problem:
#   For every number from 1 to n, decide what to output:
#     - "FizzBuzz" if the number is divisible by BOTH 3 and 5
#     - "Fizz"     if divisible by 3 (only)
#     - "Buzz"     if divisible by 5 (only)
#     - the number itself otherwise
#
# Example (n = 15):
#   1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, FizzBuzz
#
# Constraints:
#   1 <= n <= 100
#
# Hint to think about: check the "both" case FIRST. Why does the order of your
# if/elif checks matter here?
#
# Concept this builds: loops, conditionals, and the modulo operator (%).
# ---------------------------------------------------------------------------

# Write your solution below 👇
def fizzBuzz(n):
    result =[]
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    return result

if __name__ == "__main__":
    print(fizzBuzz(15))  
    print(fizzBuzz(60))