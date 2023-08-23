def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right
        
class Solution(object):
    def inorderTraversal(self, root):
        result = []
        stack = []

        while root or stack:
            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()
            result.append(root.val)
            root = root.right

        return result