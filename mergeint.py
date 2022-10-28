#!/usr/bin/env python3

import sys
from typing import List

def merge(intervals: List[List[int]]) -> List[List[int]]:
    """
    initialize an output array and sort all of the intervals by comparing their beginning elements.
    place the starting interval in the output array and for every other interval in the sorted list,
    if the beginning of the interval being considered is <= the end bound of the tail of the output arr,
    the new final bound of the current interval is the larger of the end bound of the curr interval or 
    the end of the output array. return output array
    """
    output = []

    intervals_sorted = sorted(intervals, key=lambda x: x[0])

    for interval in intervals_sorted:
        # overlap detected; new beginning less than most recent end
        if output and interval[0] <= output[-1][1]:
            # updating tail of output arr with larger bound
            output[-1][1] = max(output[-1][1], interval[1])
        else:
            output += [interval]

    return output


if __name__ == '__main__':
    assert merge([[1,3],[2,6],[8,10],[15,18]]) == [[1,6],[8,10],[15,18]]