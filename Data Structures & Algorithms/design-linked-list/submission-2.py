class ListNode:
    def __init__(self, val: int):
        self.val = val
        self.next = None
class MyLinkedList:

    def __init__(self):
        self.dummy=ListNode(-1)
        self.size=0
    def get(self, index: int) -> int:
        if index<0 or index>=self.size:
            return -1
        head=self.dummy.next
        for _ in range(index):
            head=head.next
        return head.val

    def addAtHead(self, val: int) -> None:
        head=ListNode(val)
        head.next=self.dummy.next
        self.dummy.next=head
        self.size+=1
    def addAtTail(self, val: int) -> None:
        newNode=ListNode(val)
        curr=self.dummy
        while curr.next!=None:
            curr=curr.next
        curr.next=newNode
        self.size+=1

    def addAtIndex(self, index: int, val: int) -> None:
        if index>self.size:
            return
        if index<0:
            index=0
        prev=self.dummy
        for _ in range(index):
            prev=prev.next
        newNode=ListNode(val)
        newNode.next=prev.next
        prev.next=newNode
        self.size+=1
    def deleteAtIndex(self, index: int) -> None:
        if index>=self.size or index<0:
            return
        prev=self.dummy
        for _ in range(index):
            prev=prev.next
        prev.next=prev.next.next
        self.size-=1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)