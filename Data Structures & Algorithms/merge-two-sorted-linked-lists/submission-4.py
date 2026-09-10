# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode() #dummy node, used as return, avoid edge case with empty list 
        node = dummy #used as tail, to keep track of next nodes

        while list1 and list2:
            if list1.val < list2.val: #if list1<list2, node.next = list1.val 
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            
            node = node.next
        
        node.next = list1 or list2 #condition if one list is still not empty and insert at the end of result

        return dummy.next

        #time complexity: O(n+m),n is length of list1 and m is the length of list2 
        #space complexity: O(1) 