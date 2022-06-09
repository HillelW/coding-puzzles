from typing import List

'''
   given an integer list `nums`, move all 0's 
   to the end of the list while maintaining the 
   relative order of the non-zero elements.

   Note: you must do this in-place without making a copy of the list.

    Example 1:

    Input: nums = [0,1,0,3,12]
    Output: [1,3,12,0,0]
    
    Example 2:

    Input: nums = [0]
    Output: [0]

    strategy: dynamic Fast/Trailing windowing. 
    
    first, shift all non-zero elements to the left and 
    over-write any zeros at the left side of the list.
    keep a count of how many zeros have been over-written.
    fill in missing zeros after all zeros have been over-written.
'''

# Time:  O(n), where n is the length of the list
# Space: O(1)
def move_zeros_to_end (nums: List[int]) -> None:
    # edge cases
    if not nums:
        return None
    if len (nums) == 1:
        return nums

    n = len (nums)
    # number of zeros over-written so far
    count = 0 
     
    # use second pointer to traverse the list
    for i in range (n):
        if arr[i] != 0:
             
            # clobber the zero at index `count`
            arr[count] = arr[i]
            count += 1
     
    # count now points to the index of where the first zero
    # should be. set all elements to 0 from count to the end of the list
    while count < n:
        arr[count] = 0
        count += 1
    return None
         
# driver
arr = [1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0, 9]
n = len (arr)
move_zeros_to_end (arr)
print ("Array after pushing all zeros to end of array:")
print (arr)