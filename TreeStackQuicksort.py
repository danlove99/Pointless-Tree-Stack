# Tree class

class Node(object):

	def __init__(self,value):
		self.value = value
		self.left = None
		self.right = None

class Tree(object):

	def __init__(self):
		self.root = None
		self.Stack = Stack()

	def printMe(self, Choice):
                if Choice == 'preorder':
		    self.preorder(self.root, [])
                elif Choice == 'inorder':
                    self.inorder(self.root, [])
                elif Choice == 'postorder':
                    self.postorder(self.root, [])
		temp = []
		for x in self.preStack.data:
			 temp.append(x)
		return temp
	
	def preorder(self, start, traversal):
		if start:
			self.preStack.push(start.value)
			traversal.append(start.value)
			traversal = self.preorder(start.left, traversal)
			traversal = self.preorder(start.right, traversal)
		return traversal

	def inorder(self, start, traversal):
		if start:
			traversal.append(self.preorder(start.left, traversal))
			traversal = (start.value)
			traversal = (self.preorder(start.right, traversal))
		return traversal

	def postorder(self, start, traversal):
		if start:
			traversal.append(self.preorder(start.left, traversal))
			traversal = (self.preorder(start.right, traversal))
			traversal = (start.value)
		return traversal

	def insert(self, data):
		if self.root is None:
			self.root = Node(data)
		else:
			self._insert(data, self.root)
		
	def _insert(self, data, cur_node):
		if data < cur_node.value:
			if cur_node.left is None:
				cur_node.left = Node(data)
			else:
				self._insert(data, cur_node.left)
		elif data > cur_node.value:
			if cur_node.right is None:
				cur_node.right = Node(data)
			else:
				self._insert(data, cur_node.right)
		else:
			print('value already present')




# Stack class

class Stack():

	def __init__(self):
		self.data = []

	def push(self, value):
		self.data.append(value)
		

	def pop(self):
		return self.data.pop()
		

	def get(self):
		return self.data

def quicksort(arr):
	length = len(arr)
	if length <= 1:
		return arr
	else:
		pivot = arr.pop()
	greater=[]
	lesser=[]
	for i in arr:
		if i > pivot:
			greater.append(i)
		else:
			lesser.append(i)
	return quicksort(lesser) + [pivot] + quicksort(greater)

# define a test tree

newTree = Tree()
newTree.root = Node(5)
newTree.root.left = Node(4)
newTree.root.right = Node(6)

sortedTree = Tree()

for x in (quicksort(newTree.printMe())):
	sortedTree.insert(x)
Choice = input('preorder, inorder or postorder: '
print(sortedTree.printMe(Choice))
	
