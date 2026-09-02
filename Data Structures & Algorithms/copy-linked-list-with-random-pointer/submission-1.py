"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
from collections import defaultdict
class Solution:
    def __init__(self):
        self.hmap={}
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr=head
        self.hmap[None]=None
        while curr:
            if curr not in self.hmap:
                self.hmap[curr]=Node(curr.val)
            curr=curr.next
        curr=head
        while curr:
            Node1=self.hmap[curr]
            Node1.next=self.hmap[curr.next]
            Node1.random=self.hmap[curr.random]
            curr=curr.next
        return self.hmap[head]





