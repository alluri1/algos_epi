"""
Take a input set of words and return groups of anagarms for these words.
Each group must contain at least two words
"""
import collections


def group_anagrams(dictionary):
    """
    Time complexity: O(n* m log m)
                   : n strings * sorting for each string of length m
    space complexity: O(n)
    """

    anagrams_map = collections.defaultdict(list)
    for word in dictionary:
        # sort a word by its characters
        # (sorted returns list of sorted characters, we join them to form string again)
        sorted_word = "".join(sorted(word))
        anagrams_map[sorted_word].append(word)

    output = []
    for key, value in anagrams_map.items():
        if len(value) >= 2:
            output.append(value)

    return output


input = ["debitcard", "elvis", "silent", "badcredit", "lives", "freedom", "listen", "levis", "money"]
expected = [["debitcard", "badcredit"], ["elvis", "lives", "levis"], ["silent", "listen"]]
assert expected == group_anagrams(input)
