#16.Find and display all the leaf nodes of a binary tree
class Node:
    def _init_(self,data):
        self.data = data
        self.left = None
        self.right = None
def leaf(root):
    if root:
        if root.left == None and root.right ==None:
            print(root.data)
    leaf(root.left)
    leaf(root.right)
root = None(50)
root.left = None(30)
root.right = None(70)
leaf(root)
