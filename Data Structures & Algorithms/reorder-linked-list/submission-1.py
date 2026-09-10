# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        slow = head
        fast = head
        #step 1 - find the middle element 
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        #fast is now the middle of the linked list 

        #step 2 - reverse the second half the linked list 
        curr = slow 
        prev = None 

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp 
        
        #now the second half of the linked list is reversed, prev is the head of that list 
        left = head
        right = prev

        while right.next:
            #L0 to Ln-1
            temp = left.next
            left.next = right
            left = temp
            
            #Ln-1 to L1
            temp = right.next
            right.next = left
            right = temp

            




