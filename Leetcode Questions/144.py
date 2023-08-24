class TreeNode(object):
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def preorderTraversal(self, root):
        if root is None:
            return []
        return ([root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right))
    
root = [1,None,2,3]
solution = Solution()
result = solution.preorderTraversal(root)

print(result)