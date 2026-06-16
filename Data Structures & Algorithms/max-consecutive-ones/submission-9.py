class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        i=0
        c=0
        c2=0
        while i<len(nums):
            if nums[i]==1:
                c+=1
            elif nums[i]!=1:
                c2=max(c2,c)
                c=0
            i+=1
        c2=max(c2,c)
        return c2