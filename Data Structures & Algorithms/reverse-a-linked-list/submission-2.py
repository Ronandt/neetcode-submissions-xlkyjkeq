# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head
        prev = None
        item = head
        while item.next != None:
            
            next_node = item.next
            item.next = prev
            prev = item
            item = next_node
        
        item.next = prev
        #print( item.val)
        
        return item
            


        
            

            
          


            

            

            