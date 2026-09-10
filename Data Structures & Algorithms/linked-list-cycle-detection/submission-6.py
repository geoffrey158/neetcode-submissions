# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #use a slow and fast pointer to detect a cycle
        #two pointers

        slow = head
        fast = head

        #if fast.next = None, that means there is no cycle and it ends

        while fast and fast.next:
            
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True


        return False 