"""
Given a string, check if it can be permuted to form a palindrome

Approach:
Get a frequency map of characters in the string
If the string has even length, all characters should have even frequencies
If the string has odd length, all except one character should have even frequencies
                              also at least one char should have odd frequency
"""
import collections


def can_form_palindrome(s):
    """
    Time complexity : O(n)
    Space complexity:
    O(n) worst case complexity if all keys are in hashmap
    O(c) if number of characters in the string are assumed to be constant
    """
    n = len(s)
    counter = collections.Counter(s)
    if n % 2 == 0:
        for char, freq in counter.items():
            if freq % 2 != 0:
                return False
        return True
    else:
        odd_freq = 0
        for char, freq in counter.items():
            if freq % 2 != 0:
                odd_freq += 1

        if odd_freq != 1:
            return False
        return True


input = ["edified", "aabaa", "a", ""]
output = [True, True, True]

for i, o in zip(input, output):
    print(o == can_form_palindrome(i))
