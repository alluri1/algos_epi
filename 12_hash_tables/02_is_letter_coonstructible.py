"""
Given a text for anonymous letter and text for magazine,determine if it's
possible to construct the anonymous letter using the magazine
"""
import collections


def is_letter_constructible(letter_text, magazine_text):
    """
    n - no.of letters in letter_text
    m - no.of letters in magazine_text
    Time complexity: O(n+m)
    We iterate through characters in the letter first and then magazine
    Space complexity: O(n)
    """

    letter_map = collections.Counter(letter_text)

    for magazine_char in magazine_text:
        if magazine_char in letter_map:
            letter_map[magazine_char] -= 1
            if letter_map[magazine_char] == 0:
                del letter_map[magazine_char]

    return len(letter_map) == 0


letter_text = "helloworld"
magazine_text = "llloohewrdegh"
output = True
print(is_letter_constructible(letter_text, magazine_text))