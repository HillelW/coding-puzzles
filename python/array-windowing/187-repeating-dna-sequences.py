'''
    The DNA sequence is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T'.

    For example, "ACGAATTCCG" is a DNA sequence.
    When studying DNA, it is useful to identify repeated sequences within the DNA.

    Given a string string that represents a DNA sequence, return all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule. You may return the answer in any order.

    Example 1:

    Input: string = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
    Output: ["AAAAACCCCC","CCCCCAAAAA"]
    Example 2:

    Input: string = "AAAAAAAAAAAAA"
    Output: ["AAAAAAAAAA"]

    strategy: static sliding window

    1. Search from the start of the string, and get every substring with length 10.
    2. store frequencies in a dict.
    3. return a list of strings associated with frequencies greater than 1.
'''

from typing import List


# Time:  O(n), where n is the length of the string
# Space: O(n), when all substrings of length 10 repeat
def repeating_dna_sequences (string: str) -> List[string]:
    n = len (string)
    
    # edge cases
    if not string:
        return []

    if n == 1:
        return string

    # maps substrings to frequencies
    frequencies = {}
    result = []

    # construct frequencies dict
    for i in range (n):
        substring = string[i:i+10]
        current_frequency = frequencies.get (substring, 0)
        frequencies[substring] = current_frequency + 1
    
    # check which frequencies are greater than 1 and append to result
    for key, val in frequencies.items ():
        if val > 1:
            result.append(key)
    return result