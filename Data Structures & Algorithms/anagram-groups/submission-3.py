class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=[]
        map={}
        for i,n in enumerate(strs):
            sortedS = "".join(sorted(n))
            if sortedS not in map:
                map[sortedS]=[]
            map[sortedS].append(n)
        return list(map.values())



            
