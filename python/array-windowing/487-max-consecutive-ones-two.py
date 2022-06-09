'''
Given a binary array, find the maximum number of consecutive 1s in this array if you can flip at most one 0.

Example 1:

Input: [1,0,1,1,0]
Output: 4
Explanation: Flip the first zero will get the the maximum number of consecutive 1s.
After flipping, the maximum number of consecutive 1s is 4.

This problem can be rephrased as "Find the largest window that has at most one 0 in it."
'''

from typing import List


# Time:  O(n), where n is the length of the list
# Space: O(1)
def max_consecutive_ones (nums: List[int]) -> int:
    # edge case
    if not nums or len (nums) == 0:
        return 0

    # track relevant information
    n = len (nums)
    zeros_in_window = 0
    max_window_so_far = 0

    # set initial window bounds
    left = 0
    right = 0

    # slide window and modify recorded info in each iteration
    while right < n:
        # slide right pointer and see if this causes window to become invalid
        if nums[right] == 0:
            zeros_in_window += 1 
        
        # window is good, measure it
        if zeros_in_window < 2:
            window_size = right - left + 1
            max_window_so_far = max (max_window_so_far, window_size)
        
        # window is invalid, make it valid before beginning of next iteration
        else:
            while zeros_in_window > 1:
                if nums[left] == 0:
                    zeros_in_window -= 1
                left += 1
        right += 1

    return max_window_so_far

# driver
assert max_consecutive_ones ([1,0,1,1,0]) == 4