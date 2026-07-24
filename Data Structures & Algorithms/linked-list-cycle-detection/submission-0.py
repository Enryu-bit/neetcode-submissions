# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        self.visited=0

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None:
            return False
        temp=head
        flag=0
        while temp!=None:
            if temp.visited==1:
                flag=1
                break
            temp.visited=1
            temp=temp.next
        return flag==1