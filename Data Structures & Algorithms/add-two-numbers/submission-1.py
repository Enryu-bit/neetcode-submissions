# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        c=0
        s=0
        dummy=ListNode(0)
        curr=dummy
        while l1 and l2:
            s=l1.val+l2.val+c
            if s > 9:
                c=s//10
                s=s%10
            else:
                c=0
            NodeN=ListNode(s)
            curr.next=NodeN
            curr=NodeN
            l1=l1.next
            l2=l2.next
        
        if l1:
            while l1:
                s=l1.val+c
                if s > 9:
                    c=s//10
                    s=s%10
                else:
                    c=0
                NodeN=ListNode(s)
                curr.next=NodeN
                curr=NodeN
                l1=l1.next
        if l2:
            while l2:
                s=l2.val+c
                if s > 9:
                    c=s//10
                    s=s%10
                else:
                    c=0
                NodeN=ListNode(s)
                curr.next=NodeN
                curr=NodeN
                l2=l2.next
        if c!=0:
            NodeN=ListNode(c)
            curr.next=NodeN
            curr=NodeN
        return dummy.next



