class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l=1 
        r=max(piles)
        k=r
        while l<=r:
            mid=(l+r)//2
            c=0
            f=0
            for i in range(len(piles)):
                if piles[i]%mid==0:
                    c+=piles[i]//mid
                else:
                    c+=(piles[i]//mid)+1
                if c>h:
                    f=1
                    break
            if f==0:
                k=mid
                r=mid-1
            else:
                l=mid+1
        return k


        


         

            
            

                

            

        