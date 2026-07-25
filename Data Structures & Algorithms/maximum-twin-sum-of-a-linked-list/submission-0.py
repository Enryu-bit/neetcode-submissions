# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        fast=head.next
        slow=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        l2=slow.next
        slow.next=None
        l1=head
        pvr=None
        while l2:
            nxt=l2.next
            l2.next=pvr
            pvr=l2
            l2=nxt
        tsum=0
        while l1:
            if l1.val+pvr.val >tsum:
                tsum=l1.val+pvr.val
            l1=l1.next
            pvr=pvr.next
        return tsum

