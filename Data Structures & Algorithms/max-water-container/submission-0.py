class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max=0
        for i in range(len(heights)-1):
            for j in range(i+1,len(heights)):
                if min(heights[i],heights[j])*(j-i)>max:
                    max=min(heights[i],heights[j])*(j-i)
        return max