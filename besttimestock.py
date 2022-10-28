#!/usr/bin/env python3

from re import M
import sys
from typing import List

def bestTime(nums: List[int]):
    """
    sliding window but where the critera for scrapping a window is made only until a trade is no longer "profitable" and not whether 
    the current trade is less than the current (local max) -> how you'd miss \//.  while your sell pointer is in range, calculate the profit of the trade
    if the difference between your current buy/sell window is profitable (i.e. *right > *left), see if it could be a max, otherwise (i.e. if you are not profitable),
    move the beginning of your buy window to the right.  regardless of profitability, expand your window to the right.
    """
    left, right = 0, 1
    max_profit = 0

    while right < len(nums):
        curr_profit = nums[right] - nums[left]

        # made a profit or are still profitable.
        # only stop considering when the time is no longer profitable
        # but if one day happens to not be the max, the window is still evaluated
        if nums[left] < nums[right]:
            max_profit = max(max_profit, curr_profit)

        else:
            left = right
        
        # shifting the window over
        right += 1
    
    return max_profit


if __name__ == '__main__':
    bestTime([7,1,5,3,6,4])
    bestTime([7,6,4,3,1])