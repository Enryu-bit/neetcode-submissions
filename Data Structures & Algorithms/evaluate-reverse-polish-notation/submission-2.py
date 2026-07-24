class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        a=''
        for a in tokens:
            if a=='+':
                stack.append(stack.pop()+stack.pop())
            elif a=='-':
                l1=stack.pop()
                l2=stack.pop()
                stack.append(l2-l1)
            elif a=='*':
                stack.append(stack.pop()*stack.pop())
            elif a=='/':
                l1=stack.pop()
                l2=stack.pop()
                stack.append(int(l2/l1))
            else:
                stack.append(int(a))
        return stack.pop()
            