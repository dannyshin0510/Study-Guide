# Increasing Order Search Tree

# Solution:

class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        track = [] #where we will store the ordered nums
#         we can make the list of ordered nums as list first
        def recursive(node):
            if node is None:
                return
            recursive(node.left)
            track.append(node.val)
            recursive(node.right)
        recursive(root)
#         then we make the actual returned tree
        answer = TreeNode(track[0])
        sub = answer
        for i in track[1:]: 
            sub.right=TreeNode(i)
            sub = sub.right
                
        
        return answer