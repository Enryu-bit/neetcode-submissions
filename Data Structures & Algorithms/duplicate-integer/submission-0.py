class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        map={}
        for i,n in enumerate(nums):
            if n not in map:
                map[n]=1
            else:
                return True
        return False