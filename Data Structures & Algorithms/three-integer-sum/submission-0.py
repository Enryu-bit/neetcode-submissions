class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        i=0

        matrix=[]
        for i in range(len(nums)):
            j=len(nums)-1
            k=i+1
            if nums[i]>0:
                break
            if i>0 and nums[i]==nums[i-1]:
                continue
            while k<j:
                l1=[nums[i],nums[k],nums[j]]
                if sum(l1)==0:
                    matrix.append(l1)
                    k+=1
                    j-=1
                    while k<j and nums[k]==nums[k-1]:
                        k+=1
                elif sum(l1)>0:
                    j-=1
                else:
                    k+=1
        return matrix