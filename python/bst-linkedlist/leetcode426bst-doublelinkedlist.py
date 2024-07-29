class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def convertToDLL(self, root: TreeNode) -> TreeNode:
        # Helper function to perform in-order traversal and link nodes
        def inOrderTraversal(node: TreeNode):
            nonlocal last, head
            
            if not node:
                return
            
            # Traverse the left subtree
            inOrderTraversal(node.left)
            
            # Process current node
            if last:
                last.right = node
                node.left = last
            else:
                head = node
            last = node
            
            # Traverse the right subtree
            inOrderTraversal(node.right)
        
        last = None  # Previous node in the list
        head = None  # Head of the doubly linked list
        
        # Start in-order traversal from root
        inOrderTraversal(root)
        
        return head

# Helper function to print the doubly linked list
def printDLL(head: TreeNode):
    while head:
        print(head.val, end=" <-> ")
        head = head.right
    print("None")

# Example usage:
# Create a binary search tree
#       4
#      / \
#     2   6
#    / \   \
#   1   3   5

root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(6)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.right = TreeNode(5)

solution = Solution()
dll_head = solution.convertToDLL(root)

# Print the doubly linked list
printDLL(dll_head)
