# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        current_node = head 
        node_length = 0
        while current_node != None:
            
            node_length +=1
            current_node = current_node.next
        length_to_remove = node_length - n
        node_to_remove = head
        if(length_to_remove ==0):
            return head.next
        for _ in range(length_to_remove-1):
            node_to_remove = node_to_remove.next
        before_temp = node_to_remove
        node_to_remove = node_to_remove.next
        node_to_remove_next = node_to_remove.next
        before_temp.next = node_to_remove_next
        return head
