# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        item = head
        prev = None
    
       
        while item:
            nxt = item.next
            item.next = prev
            prev = item
            item = nxt
        head = prev

        return head


            

        
            

            
          


            

            

            