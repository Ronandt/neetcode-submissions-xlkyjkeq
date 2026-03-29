import math

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        # 1. Calculate Length
        length_t = head
        length = 0
        while length_t != None:
            length_t = length_t.next
            length += 1
            
        limit = math.ceil(length / 2)

        # 2. Split the list
        node_head_to_rev = head
        # Move to the end of the first half
        for _ in range(limit - 1):
            node_head_to_rev = node_head_to_rev.next
            
        # FIX: Save the start of the second half *before* cutting the link
        second_half_start = node_head_to_rev.next
        node_head_to_rev.next = None # End the first half
        
        # 3. Reverse the second half
        prev = None
        curr = second_half_start
        while curr != None:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        
        # 'prev' is now the head of the reversed second half
        second_half = prev
        first_half = head
       
        # 4. Merge the two halves
        # We only need to check second_half because it is always shorter or equal length
        while second_half:
            tmp1 = first_half.next
            tmp2 = second_half.next
            
            first_half.next = second_half
            second_half.next = tmp1  # FIX: removed typo 'nexWht'
            
            first_half = tmp1
            second_half = tmp2