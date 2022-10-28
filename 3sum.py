#!/usr/bin/env python3

import sys
from typing import List

def threeSum(nums: List[int]) -> List[List[int]]:
    """
    sort the array in-place. iterate through the whole array making the current element fixed.
    for every iteration of the previous loop, perform two sum II on the remaining elements given they are sorted
    i.e. have a pointer to the element after curr and at the last element, if the triplet formed by the fixed number and the two pointers
    is sum == 0, add to the list, otherwise, depending on the size of the of sum relative to zero, move the left pointer forward or right back 
    """
    n = len(nums)
    triplets = set()
    nums.sort()
    
    for idx in range(n):
        left, right = idx + 1, n - 1

        while left <= right:

            triplet_sum = nums[idx] + nums[left] + nums[right]

            if idx != left != right and triplet_sum == 0:
                triplets.add([nums[idx], nums[left], nums[right]])
                left  += 1
                right -= 1

            elif triplet_sum > 0:
                right -= 1
            else:
                left += 1

    return triplets

if __name__ == '__main__':
    threeSum()