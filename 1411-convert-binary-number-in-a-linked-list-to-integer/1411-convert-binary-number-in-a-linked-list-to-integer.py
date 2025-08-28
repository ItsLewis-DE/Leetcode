# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        prev,new_head = None,head
        while new_head:
            temp = new_head.next
            new_head.next = prev
            prev = new_head
            new_head = temp
        mu =0
        res =0
        while prev:
            res += prev.val*(2**mu)
            mu+=1
            prev = prev.next
        return res