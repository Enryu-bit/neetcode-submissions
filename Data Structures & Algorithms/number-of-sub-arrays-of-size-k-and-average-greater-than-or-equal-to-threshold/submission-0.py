class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        l=0
        c=0
        for r in range(len(arr)):
            if r-l+1>k:
                l+=1
            if r-l+1==k:
                window=arr[l:l+k]
                avg=sum(window)/k
                if avg>=threshold:
                    print(l,r,"\n")
                    c+=1
        return c
        