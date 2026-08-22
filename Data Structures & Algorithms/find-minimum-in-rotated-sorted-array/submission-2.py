class Solution:
    def findMin(self, nums: List[int]) -> int:
        l=0
        r=len(nums)-1
        n=len(nums)
        for i in range(n-1):
            if nums[i%n]>nums[(i+1)%n]:
                r=i
                l=(i+1)%n
        return nums[l]


