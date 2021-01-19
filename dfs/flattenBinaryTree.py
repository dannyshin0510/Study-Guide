# Flatten Binary Tree to Linked List


class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.prev=None
        def recur (node):
            if node is None: #stop statement
                return
            recur(node.right) #traverse backwards of preorder
            recur(node.left)
            node.right = self.prev #setup in order
            self.prev = node
            node.left = None
        recur(root)