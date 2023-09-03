class Solution(object):
    def minDepth(self, root):
        if not root:
            return 0
        queue = [(root, 1)]  # Using a queue to perform BFS with depth tracking

        while queue:
            node, depth = queue.pop(0)

            # If we encounter a leaf node, return its depth
            if not node.left and not node.right:
                return depth

            # Add non-empty child nodes to the queue
            if node.left:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))