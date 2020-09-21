class Node:
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None

class BinaryTree:
	def __init__(self, root):
		self.root = Node(root)

	
	def print_tree (self, traversal_type):
		if traversal_type == "preorder":

			return self.preorder_print(tree.root, " ")
		elif traversal_type == "inorder":
			return self.inorder_print(tree.root, " ")
		elif traversal_type == "postorder":
			return self.postorder_print(tree.root, " ")
	def preorder_print(self, start, traversal):
		'''root>>>Left subtree >>>> right subtree'''


		if start:
			traversal += (str(start.value) + "-") #concatonates start.value to traversal string on every recursive call
			traversal = self.preorder_print(start.left, traversal)
			traversal = self.preorder_print(start.right, traversal)
		return traversal

	def inorder_print(self, start, traversal):
		'''left.....rooot........right'''

		if start:
			traversal = self.inorder_print(start.left, traversal)
			traversal += (str(start.value) + "-")
			traversal = self.inorder_print(start.right, traversal)
		return traversal

	def postorder_print (self, start, traversal):
		'''left....right.....root'''
		if start:
			traversal = self.postorder_print(start.left, traversal)
			traversal = self.postorder_print(start.right, traversal)
			traversal += (str(start.value) + "-")
		return traversal







''''
		    1
	   2          3
    4    5      6   7

                                                  traversal = '1-2-4-5-3-6-7'
                                                  traversal = '1-2-4-5' now returns back to original methods with original value of 1 and starts recursively applying the . right object
                                                 all left functions no longer on stack

												  traversal = '1-2 -4' start.left = 2		

												  traversal = "1-2-4"  start.left = 4
                                                  preorder print (4    "1-2-4")
												  preorder print (2    " 1 - 2   ")
                                                  preorder print(1, ' ')
												 



'''

# BUILD THE TREE
tree = BinaryTree(1)
tree.root.left = Node(2)	
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)
print(tree.print_tree("inorder"))
print(tree.print_tree("preorder"))
print(tree.print_tree("postorder"))