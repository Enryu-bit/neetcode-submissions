class MinStack:

    def __init__(self):
        self.arr=[]
        self.min=[]

    def push(self, val: int) -> None:
        self.arr.append(val)
        if not self.min:
            self.min.append(val)
        elif self.min[-1]>=val:
            self.min.append(val)

    def pop(self) -> None:
        if self.arr.pop()==self.min[-1]:
            self.min.pop()

    def top(self) -> int:
        return self.arr[-1]

    def getMin(self) -> int:
        return self.min[-1]
        
