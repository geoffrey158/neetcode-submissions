# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #get middle of linked list

        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        #slow is the middle of linked list 
        #reverse second half of linked list starting from slow 
        
        curr = slow
        prev = None 

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        #prev is the beginning of new reversed second half of the linked list 
        
        left = head 
        right = prev

        while right.next:

            #L0 -> Ln-1
            temp = left.next
            left.next = right
            left = temp 

            #Ln-1 -> L1
            temp = right.next
            right.next = left
            right = temp


