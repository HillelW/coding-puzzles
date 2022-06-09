'''
    Given a string string, find the length of the longest substring without repeating characters.

    Example 1:

    Input: string = "abcabcbb"
    Output: 3
    Explanation: The answer is "abc", with the length of 3.
    
    Example 2:

    Input: string = "bbbbb"
    Output: 1
    Explanation: The answer is "b", with the length of 1.
    
    Example 3:

    Input: string = "pwwkew"
    Output: 3
    Explanation: The answer is "wke", with the length of 3.
    Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

    strategy: dynamic Fast/Trailing windowing. 

     i
    [a, b, c, c], {a}, max == 1
     j

     i
    [a, b, c, c], {a, b}, max ==2
        j

     i
    [a, b, c, c], {a, b, c}, max == 3
           j

     i
    [a, b, c, c], {a, b}, max == 3 
              j

        i
    [a, b, c, c], {a}, max == 3 
              j

        i
    [a, b, c, c], {a}, max == 3 
              j
'''

# Time:  O(n), where n is the length of the string
# Space: O(1), since the set can only contain alphabetic letters
def length_of_longest_substring (string: str) -> int:
    # edge cases
    if string == '':
        return 0
    
    if len (string) == 1:
        return 1

    # track relevant information
    n = len (string)
    max_so_far = 0
    unique_characters = set ()

    # set initial window bounds
    left = 0
    right = 0

    # traverse the string once
    while right < n:
        # window is good - measure it
        if string[right] not in unique_characters:
            unique_characters.add (string[right])
            right += 1
            max_so_far = max (max_so_far, len(unique_characters))
         # window is invalid - move left to see if window becomes valid
        else:
            unique_characters.remove (string[left])
            left += 1
    return max_so_far

# driver
assert length_of_longest_substring ('abcabcbb') == 3 
assert length_of_longest_substring ('bbbbb') == 1
assert length_of_longest_substring ('pwwkew') == 3 