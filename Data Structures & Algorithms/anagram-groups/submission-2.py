class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=[]
        map={}
        for i,n in enumerate(strs):
            s="".join(sorted(n))
            if s not in map:
                map[s]=[]
            else:
                continue
        for i,n in enumerate(strs):
            if("".join(sorted(n))) in map:
                map["".join(sorted(n))].append(n)
        print(map)

        for key,value in map.items():
            res.append(value)
        return res



            
