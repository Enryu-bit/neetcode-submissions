# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr=ListNode(0,None)
        if list1==None:
            return list2
        if list2==None:
            return list1
        if list1.val<=list2.val:
            curr=list1
            list1=list1.next
        else:
            curr=list2
            list2=list2.next
        temp=ListNode(0,None)
        curr.next=temp
        head=curr
        while list1!=None and list2!=None :
            if(list1.val<=list2.val):
                temp=list1
                list1=list1.next
            else:
                temp=list2
                list2=list2.next
            curr.next=temp
            curr=temp
        if list1!=None:
            curr.next=list1
        if list2!=None:
            curr.next=list2
        return head
            
                
        