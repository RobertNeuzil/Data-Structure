'''

head pointer starts at first node in list
node carries DATA and NEXT position in memory
end of list is null
'''

class Node(object):
	"""docstring for Node"""
	def __init__(self, data = None, next_n = None):
		self.data = data
		self.next_n = next_n
		

class TheList(object):
	"""docstring for TheList"""
	def __init__(self, head = None):
		self.head = head
		
	def insert(self, data):
		new_node = Node(data)

		if self.head is None:
			self.head = new_node
			return
		
		current_node = self.head
		
		if current_node.next_n is None:
			current_node.next_n = new_node
			return
		
		current_node = current_node.next_n

		while current_node:
			current_node.next_n = new_node
			break
	
	def print (self):
		bouncer = self.head
		print (f'{bouncer.data}')
		bouncer = bouncer.next_n
		print (f'{bouncer.data}')
		print (f'{bouncer.data}')
		bouncer = bouncer.next_n
		print (f'{bouncer.data}')

		


llist = TheList()
llist.insert(5)
llist.insert(6)
llist.insert(7)
llist.print()


'''
Node1 >>> 3  >>>> Node2 7 >>>> Node3 25 >>>> None
'''

#current_node = node1

'''
while True:
	print (f'{current_node.data} >>>')
	if current_node.next_node is None:
		print ("None")
		break
	current_node = current_node.next_node
'''