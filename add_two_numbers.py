#!/usr/bin/env python3

from re import L
import sys
from typing import List
  
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __repr__(self):
        vals = []

        ptr = self
        while ptr.next:
            vals.append(self.val)
            ptr = ptr.next
        
        return "->".join(map(str, vals))
            
    
def addTwoNumbers(l1, l2):
    """
    initialize an pointer to a new linked list

    knowing in advance the edge case, iterate while there is still reason to (i.e. a list still exists or there's a carry)
    get the value of the actual addition, and extract what will be the value actually stored at the node and the carry 
    (while at the same time priming any empty values for use in later iterations)
    update solution list and advance pointers of solution and input lists
    """

    # 2 pointers to the beginning of our solution list; one will 
    # keep the reference and the other will iteratively build the list
    curr_ptr = head = ListNode()
    # in order to generalize the procedure for addition, we need the 
    # carry value to be initialized/exist
    carry = 0

    # loop as long as there are values to add (this will work because we 
    # check for existence as well as plug with zeros)
    while l1 or l2 or carry:
        # carry necessary for edge case because the final sum could have a carry
        # digit that wouldnt be caught 

        # could be one line but need to do checking
        v1 = l1.val if l1 else 0
        v2 = l2.val if l2 else 0 

        node_sum = v1 + v2 + carry
        
        # extract value; only one that becomes the node value is the one's place
        node_val = node_sum % 10

        # determine carry (if any); updating it for future iterations of the loop
        carry = node_sum // 10

        # create new node and append to solution list
        curr_ptr.next = ListNode(node_val)

        # advance pointers
        # necessary for list to actually grow 
        # (since you will otherwise keep replacing the same pointer)
        curr_ptr = curr_ptr.next
        # explicitly defining next as None so that v1/v2 calculations happen
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

    # node was initially defined as a dummy
    return head.next  

if __name__ == '__main__':
    print(addTwoNumbers(
        ListNode(2, ListNode(4, ListNode(3, None))),
        ListNode(5, ListNode(6, ListNode(4, None)))
        ))
