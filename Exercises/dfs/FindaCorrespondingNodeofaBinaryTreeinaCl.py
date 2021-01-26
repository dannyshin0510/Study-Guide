# Find a Corresponding Node of a Binary Tree in a Clone of That Tree


# Given two binary trees original and cloned and given a reference to a node target in the original tree.

# The cloned tree is a copy of the original tree.

# Return a reference to the same node in the cloned tree.

# Note that you are not allowed to change any of the two trees or the target node and the answer must be a reference to a node in the cloned tree.

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        
        def recurse(cloneNode, oriNode):
            if cloneNode is None:
                return
            if oriNode == target:
                return cloneNode
        
            return recurse(cloneNode.left, oriNode.left) or recurse(cloneNode.right, oriNode.right)
        return recurse(cloned, original)