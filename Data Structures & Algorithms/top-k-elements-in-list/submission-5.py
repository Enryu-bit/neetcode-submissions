from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map=defaultdict(int)
        for i in range(len(nums)):
            map[nums[i]]+=1
        dict_sorted=dict(sorted(map.items(),key=lambda item:item[1],reverse=True))
        c=0
        res=[]
        for key,value in dict_sorted.items():
            if c<k:
                res.append(key)
                c+=1
            else:
                break
        return res
            

