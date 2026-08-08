from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        arr=s
        l=0
        max_len=0
        r=0
        window=defaultdict(int)
        while r<len(arr):
            window[arr[r]]+=1
            while window[arr[r]]>1:
                window[arr[l]]-=1
                l+=1
            max_len=max(max_len,(r-l+1))
            r+=1
        return max_len