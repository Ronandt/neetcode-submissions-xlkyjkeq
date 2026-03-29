# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import math
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        length_t = head
        #assume that there's a head
        length = 0
        while length_t!= None:
           
            length_t = length_t.next
            length+=1
        limit = math.ceil(length/2)

        node_head_to_rev = head
  

   
        for _ in range(limit-1):
            node_head_to_rev = node_head_to_rev.next

        second_half = node_head_to_rev.next
        node_head_to_rev.next = None

        prev = None
  

        # --- CHANGE 2: reverse second half using existing variable names ---
        prev = None
        while second_half != None:
            tmp = second_half.next
            second_half.next = prev
            prev = second_half
            second_half = tmp

        # --- CHANGE 3: merge ---
        first_half = head
        second_half = prev  # head of reversed second half
       
        while first_half != None and second_half != None:
            tmp = first_half.next
            first_half.next = second_half
            first_half = tmp
            tmp = second_half.next
            second_half.next = first_half
            second_half = tmp

        
        
        