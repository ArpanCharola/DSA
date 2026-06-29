# ---------------------------------------------------------------------------
# COUNT VOWELS
# ---------------------------------------------------------------------------
# Problem:
#   Given a string, count how many vowels (a, e, i, o, u) it contains.
#
# Examples:
#   "education"  ->  5      (e, u, a, i, o)
#   "rhythm"     ->  0
#   "AEIOU"      ->  5      (treat uppercase as vowels too)
#
# Constraints:
#   0 <= len(s) <= 1000
#
# STRETCH: instead of a single total, return a dict with each vowel's count:
#   "education" -> {'a': 1, 'e': 1, 'i': 1, 'o': 1, 'u': 1}
#   This is your first real use of a dict as a "counter" — a core DSA tool.
#
# Concept this builds: iteration, membership checks (the `in` keyword),
# and using a dict / hashmap as a counter.
# ---------------------------------------------------------------------------

# Write your solution below 👇
def count_vowels(s):
    vowels = 'aeiouAEIOU'
    count = 0
    for char in s:
        if char in vowels:
            count+=1
    return count

def count_vowels_dict(s):
    vowels = 'aeiouAEIOU'
    vowel_count = {vowel.lower(): 0 for vowel in vowels if vowel.islower()}
    for char in s:
        if char in vowels:
            vowel_count[char.lower()] += 1
    return vowel_count

if __name__ == "__main__":
    test_string = "Master Jiraiya"
    print(f"Total vowels in '{test_string}': {count_vowels(test_string)}")
    print(f"Vowel counts in '{test_string}': {count_vowels_dict(test_string)}")