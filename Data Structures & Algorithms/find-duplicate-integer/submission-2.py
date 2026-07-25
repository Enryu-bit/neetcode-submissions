class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        i=0
        j=1
        while True:
            if i==j:
                j=(j+1)%len(nums)
            if nums[i]==nums[j]:
                return nums[i]
            i=(i+1)%len(nums)
            j=(j+2)%len(nums)