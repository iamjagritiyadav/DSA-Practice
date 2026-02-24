class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node, current):
            if not node:
                return 0
            
            # Build binary number
            current = current * 2 + node.val
            
            # If leaf node, return current number
            if not node.left and not node.right:
                return current
            
            # Recurse left and right
            return dfs(node.left, current) + dfs(node.right, current)
        
        return dfs(root, 0)
