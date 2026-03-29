# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        tortoise = head
        hare = head
        if head == None:
            return False
        while True:
            if(tortoise.next != None):
                tortoise = tortoise.next
            
            for x in range(2):
                if(hare.next != None):
                    hare = hare.next
                else:
                    return False

            if tortoise == hare:
                return  True
