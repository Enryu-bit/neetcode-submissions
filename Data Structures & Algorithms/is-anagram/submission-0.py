class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        map1={}
        map2={}
        for i,n in enumerate(s):
            if n not in map1:
                map1[n]=1
            else:
                map1[n]+=1
        for i,n in enumerate(t):
            if n not in map1:
                return False
            else:
                if n not in map2:
                    map2[n]=1
                else:
                    map2[n]+=1
        return map1==map2

                
                