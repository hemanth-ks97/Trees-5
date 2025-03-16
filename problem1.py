"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
# Time Complexity : O(n), n-> nodes in tree
# Space Complexity : O(1)
# Did this code successfully run on Leetcode : YES

# Any problem you faced while coding this : NO
class BFSSolution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
            
        level = root

        while level.left:
            cur = level
            while cur:
                cur.left.next = cur.right
                if cur.next:
                    cur.right.next = cur.next.left
                cur = cur.next
            level = level.left
        
        return root

# Time Complexity : O(n), n-> nodes in tree
# Space Complexity : O(h)
# Did this code successfully run on Leetcode : YES

# Any problem you faced while coding this : NO
class DFSSolution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None

        def dfs(left, right):
            # base
            if not left or not right:
                return
            # logic
            left.next = right
            dfs(left.left, left.right)
            dfs(left.right, right.left)
            dfs(right.left, right.right)
        
        dfs(root.left, root.right)
        return root


# Time Complexity : O(n), n-> nodes in tree
# Space Complexity : O(hxs)
# Did this code successfully run on Leetcode : YES

# Any problem you faced while coding this : NO

class BetterDFSSolution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None

        def dfs(root):
            # base
            if not root.left:
                return
            
            # logic
            root.left.next = root.right
            if root.next:
                root.right.next = root.next.left
            dfs(root.left)
            dfs(root.right)
        
        dfs(root)
        return root