#!/usr/bin/env python3

import sys
from typing import List


def maxSubarray(nums: List[int]) -> int:
    """
    O(n^2) solution: 
    """

    cur_sum, max_sum = 0, float('-inf')

    for i in range(len(nums)):
        cur_sum = nums[i]
        max_sum = max(max_sum,cur_sum)

        for j in range(i+1,len(nums)):
            cur_sum += nums[j]
            max_sum = max(max_sum,cur_sum)

    return max_sum

def kadane(nums: List[int]) -> int:
    """
    O(n) solution: iterate through every number. the current max sum will either be 
    the array up to this point (including the current element), or just the 
    current element if it is necessary to start a new array.  
    for every new sum computed, it's possible that it could be the max till now, 
    and it is necessary to check and update to get the solution.
    """
    cur_max, max_till_now = 0, float('-inf')

    for c in nums:
        cur_max = max(c, cur_max + c)
        max_till_now = max(max_till_now, cur_max)

    return max_till_now



if __name__ == '__main__':
    assert kadane([-2,1,-3,4,-1,2,1,-5,4]) == 6
    assert kadane([1]) == 1
    assert kadane([5,4,-1,7,8]) == 23
    print(kadane([-2,1,-3,4,-1,2,1,-5,4]))