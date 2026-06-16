# ---------------------------------------------------------------------------
# LARGEST NUMBER IN A LIST
# ---------------------------------------------------------------------------
# Problem:
#   Given a list of numbers, return the largest one.
#   IMPORTANT: do NOT use the built-in max(). Build the logic yourself.
#
# Examples:
#   [3, 9, 2, 7]        ->  9
#   [-5, -1, -10]       ->  -1     (works with negatives!)
#   [42]                ->  42
#
# Constraints:
#   1 <= len(nums) <= 1000
#   The list always has at least one number.
#
# Hint: "scan and remember." Start by assuming the first element is the biggest,
# then walk through the rest and update your "biggest so far" whenever you find
# something larger. Careful: don't start your guess at 0 — why would that break
# the all-negatives example?
#
# Concept this builds: linear scan + tracking state in a variable. This exact
# pattern powers tons of array algorithms (max subarray, min cost, etc.).
# ---------------------------------------------------------------------------

# Write your solution below 👇
