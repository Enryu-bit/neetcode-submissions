# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMin(self,root)->int:
        curr=root
        while curr.left:
            curr=curr.left
        return curr.val
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        if key>root.val:
            root.right=self.deleteNode(root.right,key)
        elif key<root.val:
            root.left=self.deleteNode(root.left,key)
        else:
            if root.right is None:
                return root.left
            elif root.left is None:
                return root.right
            else:
                root.val=self.findMin(root.right)
                root.right=self.deleteNode(root.right,root.val)
        return root