# Count Good Nodes in Binary Tree

# Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.

# Return the number of good nodes in the binary tree.

class Solution:
    answer = 0 #so that we can always access this var in the recursion
    def goodNodes(self, root: TreeNode) -> int:
        
        def recursive(node, lgst):
            if not node:
                return
            if node.val>=lgst:
                self.answer +=1
                lgst=node.val
            recursive(node.left, lgst)
            recursive(node.right, lgst)
        recursive(root, root.val)
        return self.answer