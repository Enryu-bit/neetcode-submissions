class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        top=-1
        f=0
        for a in s:
            if a=='{' or a=='['or a=='(':
                stack.append(a)
                top+=1
            elif a=='}'or a==')'or a==']':
                if top==-1:
                    return False
                s1=stack.pop()
                top-=1
                if not((a=='}'and s1=='{')or(a==']'and s1=='[')or(a==')'and s1=='(')):
                    f=1
                    break
        if top==-1 and f==0:
            return True
        else:
            return False
                
        