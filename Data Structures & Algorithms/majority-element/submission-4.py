class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        can = None
        count = 0
        for num in nums:
            if count==0:
                can = num
            count +=1 if can == num else -1

        return can