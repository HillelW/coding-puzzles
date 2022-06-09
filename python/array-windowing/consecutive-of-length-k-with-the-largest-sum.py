'''
given an integer array nums and an integer, 
find a consecutive subarray of nums of length k that has the largest sum.

returns the solution as an integer array of length k.

Example 1:

Input: nums = [2,1,3,3], k = 2
Output: [3,3]

Explanation:
The subarray has the largest sum of 3 + 3 = 6.

Example 2:

Input: nums = [3,4,3,3], k = 2
Output: [3,4]

Explanation:

The subarray has the largest sum of 3 + 4 = 7. 
Another possible subsequence is [4, 3].
'''

from typing import List


# Time:  O(n*k), where n is the length of the list
# Space: O(1)
def max_consecutive_brute_force (nums: List[int], k: int) -> List[int]:
    '''strategy: iterate through all windows of size k'''
    if len (nums) == 0:
        return []

    if len (nums) == 1:
        return nums

    n = len (nums)
    
    # initialize max so far to first subarray
    max_sum_so_far = sum (nums[:k])
    left = 0
    right = k-1

    for i in range (n-k+1):
        current_sum = sum (nums[i:i+k])
        if current_sum > max_sum_so_far:
            max_sum_so_far = current_sum
            left = i
            right = i + k - 1
    return nums[left: right+1]

# Time:  O(n), where n is the length of the list
# Space: O(1)
def max_consecutive_fast (nums: List[int], k: int) -> List[int]:
    '''strategy: do not re-compute the entire sum each time the window moves'''
    if len (nums) == 0:
        return []

    if len (nums) == 1:
        return nums

    n = len (nums)

    left_result = 0
    right_result = k-1

    max_sum_so_far = sum (nums[left_result: right_result + 1])
    current_sum = sum (nums[left_result: right_result + 1])

    left = left_result
    right = right_result

    while right < n-k+1:
        left +=1
        right +=1

        current_sum = current_sum - nums[left-1] + nums[right] 

        if current_sum > max_sum_so_far:
            max_sum_so_far = current_sum
            left_result = left
            right_result = right 
    return nums[left_result: right_result+1]

# driver
assert max_consecutive_brute_force ([2,1,3,3], 2) == [3, 3]
assert max_consecutive_brute_force ([3,4,3,3], 2) == [3, 4]

assert max_consecutive_fast ([2,1,3,3], 2) == [3, 3]
assert max_consecutive_fast ([3,4,3,3], 2) == [3, 4]