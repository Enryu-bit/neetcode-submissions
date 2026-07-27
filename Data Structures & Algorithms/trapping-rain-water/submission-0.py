class Solution:
    def trap(self, height: List[int]) -> int:
        i=1
        water=0
        maxL=[0]*len(height)
        maxL[0]=height[0]
        maxR=[0]*len(height)
        j=len(height)-2
        maxR[j+1]=height[j+1]

        while i<len(height):
            if height[i]>maxL[i-1]:
                maxL[i]=height[i]
            else:
                maxL[i]=maxL[i-1]

            if height[j]>maxR[j+1]:
                maxR[j]=height[j]
            else:
                maxR[j]=maxR[j+1]
            i+=1
            j-=1
        i=0
        print(maxL)
        print(maxR)
        while i<len(height):
            water+=min(maxL[i],maxR[i])-height[i]
            i+=1
        return water   
