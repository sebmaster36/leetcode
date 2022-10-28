#!/usr/bin/env python3

import sys
from typing import Dict

def lengthOfLongestSubstring(s: str) -> int:
    """
    O(n) sliding window with a hash data structure to keep track 
    of most recently seen/working character.
    

    keep a dictionary of the locations of all seen characters as well as keep a pointer to the head of the current subsequence
    and the length of the longest sum.  for every character we see, we make sure we havent seen it in this sequence, if we have, 
    that means we break, and on break we evaluate candiddacy as the largest seuquence, and perhaps update the max.  omce your sequence breaks,
    you must start a new one, and the approproate place to do so is the element right after he element which broke the sequence.
    independent of seen, update the seenness of every character.  there is an edge case at the very end of list of charcters, which is the 
    potential for an unseen character to be a potential canditiate contributor. return the length of largest seuqnce 
    (its posisble its the length of the current subsequence + final char)
    """
    
    seen: Dict[int, int] = {}
    max_len: int = 0
    head_idx: int = 0

    for idx, char in enumerate(s):

        # repeated character seen in the current substring (i.e. break the substring)
        if char in seen and seen.get(char) >= head_idx:
            curr_len: int = idx - head_idx

            # updating global max if necessary
            if curr_len > max_len:
                max_len = curr_len

            # update beginning of the window to the position right after offending char
            head_idx = seen.get(char) + 1

        # last position of current element updated
        seen[char] = idx

    # edge case: unseen char found at end of string, consequence of implementation
    curr_len = len(s) - head_idx

    return max(curr_len, max_len)


if __name__ == '__main__':
    lengthOfLongestSubstring("abcabcbb")
    lengthOfLongestSubstring("bbbbb")
    lengthOfLongestSubstring("pwwkew")