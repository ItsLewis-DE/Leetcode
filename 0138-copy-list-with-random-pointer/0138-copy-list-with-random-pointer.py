"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hash = collections.defaultdict(lambda:Node(0))
        hash[None] = None
        cur = head
        while cur:
            hash[cur].val = cur.val
            hash[cur].next = hash[cur.next]
            hash[cur].random = hash[cur.random]
            cur = cur.next
        return hash[head]