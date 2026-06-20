class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack=[]
        for a in operations:
            if a=='+':
                o1=stack[-1]
                o2=stack[-2]
                stack.append(o1+o2)
            elif a=='C':
                stack.pop()
            elif a=='D':
                stack.append(stack[-1]*2)
            else:
                stack.append(int(a))
        return sum(stack)