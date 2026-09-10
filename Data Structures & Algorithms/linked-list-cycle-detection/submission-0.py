# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        while fast and fast.next: #if fast reaches the end that means there is no cycle
            slow = slow.next
            fast = fast.next.next
            if slow == fast: #if slow ever catches up to fast there means there is a cycle 
                return True
            
        return False

