# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp=head
        pvr=None
        while temp:
            nxt=temp.next
            temp.next=pvr
            pvr=temp
            temp=nxt
        dummy=ListNode(0)
        dummy.next=pvr
        curr=dummy
        for _ in range(n-1):
            curr=curr.next
        curr.next=curr.next.next
        temp=dummy.next
        pvr=None
        while temp:
            nxt=temp.next
            temp.next=pvr
            pvr=temp
            temp=nxt
        return pvr