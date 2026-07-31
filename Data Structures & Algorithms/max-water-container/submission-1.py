class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i=0
        j=len(heights)-1
        m=-1
        while i<j:
            res=min(heights[i],heights[j])*(j-i)
            m=max(res,m)
            if heights[i]<=heights[j]:
                i+=1
            else:
                j-=1
        return m