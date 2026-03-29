# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_current = l1
        l2_current = l2
        #assume that the numbers are same number
        dummy = ListNode() #dummy
        current = dummy
        build_total = []
        leftover = 0
        while l1_current != None and l2_current !=None:
            total = l1_current.val + l2_current.val + leftover
            print(l1_current.val, l2_current.val)
            stringified = str(total)[::-1]
            if len(stringified[1:]) > 0:
                leftover= int(stringified[1:])
            else:
                leftover = 0
            build_node = ListNode(val =int(stringified[0] ))
            current.next = build_node
            current = current.next
           
            l1_current = l1_current.next
            l2_current = l2_current.next
        
      
        while l1_current !=None:
            total = l1_current.val + leftover
            stringified = str(total)[::-1]
            if len(stringified[1:]) > 0:
                leftover = int(stringified[1:])
            else:
                leftover = 0    
            build_node = ListNode(val = int(stringified[0]))
            current.next = build_node
            current = current.next
            l1_current = l1_current.next
        while l2_current != None:
            total = l2_current.val + leftover
            stringified = str(total)[::-1]
            if len(stringified[1:]) > 0:
                leftover = int(stringified[1:])
            build_node = ListNode(val = int(stringified[0]))
            current.next = build_node
            current = current.next
            l2_current = l2_current.next
        stringified_leftover = str(leftover)
        for x in range(len(stringified_leftover)):
            if  stringified_leftover[x] != "0" or x != len(stringified_leftover)-1:
                build_node = ListNode(val = int(stringified_leftover[x]))
                current.next = build_node
                current = current.next

        return dummy.next