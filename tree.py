class node():
	def __init__(self, d):
		self.data = d
		self.left = None
		self.right = None
	
	def insert(self, d):		
		if self.data == d:
			return False
		if d < self.data:
			if self.left:
				return self.left.insert(d)
			self.left = node(d)
			return True
		if d > self.data:
			if self.right:
				return self.right.insert(d)
			self.right = node(d)
			return True	
				
	def find(self, d):
		if self.data:
			if self.data == d:
				return d
			if d < self.data:
				if self.left:
					return self.left.find(d) 
				return False
			if d > self.data:
				if self.right:
					return self.right.find(d)
				return False
		return False

	def preorder(self):	
		print(str(self.data))
		if self.left:
			self.left.preorder()
		if self.right:
			self.right.preorder()

	def postorder(self):
		if self.left:
			self.left.postorder()
		if self.right:
			self.right.postorder()
		print(str(self.data))

	def inorder(self):
		if self.left:
			self.left.inorder()
		print(str(self.data))
		if self.right:
			self.right.inorder()

	def delete(self, d):
		parent = None
		node = self
		print(node.left.data,node.right.data)
		while node and node.data != d:
			parent = node
			if d < node.data:
				node = parent.left
			elif d > node.data:
				node = parent.right
		if node == None:
			return False

		#case 1: node has no child
		if node.left == None and node.right == None:	
			if node.data > parent.data:
				parent.right = None
			elif node.data <	parent.data:
				parent.left = None
		
		#case 2: node has 1 left child
		elif node.left and node.right == None:
			if node.data > parent.data:
				parent.right = node.left
			elif node.data < parent.data:
				parent.left = node.left
		
		#case 3: node has 1 right child
		elif node.right and node.left == None:
			if node.data > parent.data:
				parent.right = node.right
			elif node.data < parent.data:
				parent.left = node.right
		
		#case 4: node has both children
		elif node.left and node.right:
			delparent = node
			delnode = node.right
			while delnode.left != None:
				delparent = delnode
				delnode = delnode.left
			print("delnode is",delnode.data)
			if delnode.right:
				node.data = delnode.data
				delparent.left = delnode.right
			else:
				node.data = delnode.data
				delparent.left = None

class tree():
	def __init__(self):
		self.root = None
	
	def insert(self, d):
		if self.root:
			return self.root.insert(d)
		self.root = node(d)
		return True
	def find(self, d):
		if self.root:
			return self.root.find(d)
		return False
	def preorder(self):
		if self.root:
			print("preorder")
			return self.root.preorder()
	def postorder(self):
		if self.root:
			print("postorder")
			return self.root.postorder()
	def inorder(self):
		if self.root:
			print("inorder")
			return self.root.inorder()
	def delete(self, d):
		if self.root:
			return self.root.delete(d)
		else:
			return False

def main():
	bst = tree()
	print(bst.insert(11))
	bst.insert(6)
	bst.insert(19)
	bst.insert(4)
	bst.insert(9)
	bst.insert(7)
	bst.insert(8)
	bst.preorder()
	bst.postorder()
	bst.inorder()
	print("14", bst.find(14))
	print("15", bst.find(15))
	bst.delete(6)
	bst.inorder()

main()
