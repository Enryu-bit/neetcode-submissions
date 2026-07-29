class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        map={}
        c=len(nums)//2
        if len(nums)==1:
            return nums[0]
        for i,n in enumerate(nums):
            if n not in map:
                map[n]=1
            else:
                map[n]+=1
                if map[n]>c:
                    break
        return n
            
