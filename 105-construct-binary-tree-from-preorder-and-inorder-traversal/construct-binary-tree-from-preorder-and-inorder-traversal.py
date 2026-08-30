# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        imap = {}
        pre = 0

        for i in range(len(inorder)):
            imap[inorder[i]] = i
        
        def construct(l, r):
            nonlocal pre

            if l > r:
                return None

            root = TreeNode()

            root.val = preorder[pre]
            pre += 1
            root.left = construct(l, imap[root.val] - 1)
            root.right = construct(imap[root.val] + 1, r)

            return root
        
        return construct(0, len(inorder) - 1)
