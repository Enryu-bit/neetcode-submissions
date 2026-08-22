# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q=deque()
        res=[]
        if root:
            q.append(root)
        while q:
            arr=[]
            qLen=len(q)
            for i in range(qLen):
                curr=q.popleft()
                if curr:
                    arr.append(curr.val)
                    q.append(curr.left)
                    q.append(curr.right)
            if arr:
                res.append(arr)
        return res
                
            
