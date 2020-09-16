'''
stack data structure
'''


class Stack():
	"""docstring for Stack"""
	def __init__(self):
		self.items = []

	def push(self, item):
		self.items.append(item)
	
	def pop(self):
		return self.items.pop()
	
	def get_stack(self):
		return self.items

	def remove_item(self, item):
		return self.items.remove(item)

	def is_empty(self):
		if len(self.items) == 0:
			return True
		else:
			return False
	
	def peak(self):
		return self.items[-1]

'''
s = Stack()
lol = Stack()

print (s.is_empty())
s.push("A")
s.push("B")
s.push("C")
print (s.is_empty())

print (s.peak())'''