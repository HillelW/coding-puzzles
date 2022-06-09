'''
Given a binary array nums, return the maximum number of consecutive 1's in the array.

Example 1:

Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. 
The maximum number of consecutive 1s is 3.

Example 2:

Input: nums = [1,0,1,1,0,1]
Output: 2
'''

from typing import List


# Time:  O(n), where n is the length of the list
# Space: O(1)
def find_max_consecutive_ones (nums: List[int]) -> int:
    '''
       strategy: keep incrementing the counter until a zero is found.
       when a zero is found, reset the counter to 0.
    '''
    n = len (nums)
    
    if not nums or n == 0:
        return []
    
    if nums == 1:
        return nums

    max_so_far = 0
    count = 0

    for num in nums:
        if num == 1:
            count += 1
            max_so_far = max (max_so_far, count)
        else:
            count = 0
    return max_so_far

# driver
assert find_max_consecutive_ones ([1,1,0,1,1,1]) == 3
assert find_max_consecutive_ones ([1,0,1,1,0,1]) == 2