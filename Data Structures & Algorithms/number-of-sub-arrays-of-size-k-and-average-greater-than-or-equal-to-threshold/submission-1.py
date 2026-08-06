class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        window_sum=0
        c=0
        target=k*threshold
        for r in range(len(arr)):
            window_sum+=arr[r]
            if r>=k:
                window_sum-=arr[r-k]
            if r>=k-1 and window_sum>=target:
                c+=1
        return c