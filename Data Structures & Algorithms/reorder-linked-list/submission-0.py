# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
            slow,fast=head,head.next
            while fast and fast.next:
                slow=slow.next
                fast=fast.next.next
            second=slow.next
            slow.next=None
            pvr=None
            while second:
                nxt=second.next
                second.next=pvr
                pvr=second
                second=nxt
            curr=head
            while pvr:
                n1=curr.next
                n2=pvr.next
                pvr.next=curr.next
                curr.next=pvr
                curr=n1
                pvr=n2
