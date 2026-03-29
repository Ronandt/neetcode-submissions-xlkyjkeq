# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        list1_prog = list1
        list2_prog = list2
        head = ListNode()
        current = head
        
        if list1_prog == None:
            return list2_prog
        elif list2_prog == None:
            return list1_prog


        while list1_prog != None and list2_prog!=None:
            temp = ListNode()
            if(list1_prog.val >= list2_prog.val):
                temp.val = list2_prog.val
                list2_prog = list2_prog.next
            else:
                temp.val = list1_prog.val
                list1_prog = list1_prog.next

            current.next = temp
            current = temp
       
        while list1_prog != None:
            additional_temp = ListNode()
            additional_temp.val = list1_prog.val
            list1_prog = list1_prog.next
            current.next = additional_temp
            current = additional_temp
        while list2_prog !=None:
            additional_temp = ListNode()
            additional_temp.val = list2_prog.val
            list2_prog = list2_prog.next
        
            current.next = additional_temp
            current = additional_temp
        print(list2_prog, list1_prog, current.val)

                
        return head.next



            

        