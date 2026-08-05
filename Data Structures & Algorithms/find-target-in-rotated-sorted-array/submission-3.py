class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l=0
        r=len(nums)-1
        while l<r:
            mid=l+(r-l)//2
            if nums[mid]<nums[r]:
                r=mid
            else:
                l=mid+1
        ls=nums[l:]+nums[0:l]
        left=0
        right=len(ls)-1
        c=-1
        while left<=right:
            mid=left+(right-left)//2
            if ls[mid]<target:
                left=mid+1
            elif ls[mid]>target:
                right=mid-1
            else:
                c=mid
                break
        print(ls)
        if c==-1:
            return -1
        else:
            return (c+l)%len(nums)
