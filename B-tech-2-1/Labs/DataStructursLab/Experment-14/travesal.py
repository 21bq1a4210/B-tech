class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def printInorder(root):
    if root:
        # First recur on left child
        printInorder(root.left)
        # then print the data of node
        print(root.val,end=' '),
        # now recur on right child
        printInorder(root.right)
 
def printPreorder(root):
    if root:
        # First print the data of node
        print(root.val,end=' '),
        # Then recur on left child
        printPreorder(root.left) 
        # Finally recur on right child
        printPreorder(root.right)
      
def printPostorder(root):
    if root: 
        # First recur on left child
        printPostorder(root.left)
        # the recur on right child
        printPostorder(root.right)
        # now print the data of node
        print(root.val,end=' '),

# Driver code
if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
 
    # Function call
    print("\nInorder traversal of binary tree is:")
    printInorder(root)
    print("\nPreorder traversal of binary tree is:")
    printPreorder(root)
    print("\nPostoreder traversal of binary tree is:")
    printPostorder(root)