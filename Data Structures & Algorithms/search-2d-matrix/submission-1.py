class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l=0
        r=len(nums)-1
        mid=0
        while l<=r:
            mid=(l+r)//2
            if nums[mid]>target:
                r=mid-1
            if nums[mid]<target:
                l=mid+1
            if nums[mid]==target:
                return True
        return False
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r=len(matrix)
        c=len(matrix[0])
        if target>matrix[r-1][c-1]:
            return False
        if target<matrix[0][0]:
            return False
        t=0
        d=r-1
        while t<=d:
            mid=(t+d)//2
            if matrix[mid][0]<=target and matrix[mid][c-1]>=target:
                return self.search(matrix[mid],target)
            else:
                if matrix[mid][0]<target:
                    t=mid+1
                if matrix[mid][0]>target:
                    d=mid-1
        return False
        