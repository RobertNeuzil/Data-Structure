from stackdatastructure import Stack

'''
0 1 2 4 8 16 32 64 128

'''
class IntegerToBinary(Stack):
	def __init__(self,num):
		self.stack = []
		self.num = num

	def convert(self):
		if self.num >  256:
			print ("No. Go Somewhere else")

		elif self.num < 256:
			self.stack.append(self.num % 2)
			self.num = self.num // 2
			self.stack.append(self.num % 2)
			self.num = self.num // 2
			self.stack.append(self.num % 2)
			self.num = self.num // 2
			self.stack.append(self.num % 2)
			self.num = self.num // 2
			self.stack.append(self.num % 2)
			self.num = self.num // 2
			self.stack.append(self.num % 2)
			self.num = self.num // 2
			self.stack.append(self.num % 2)
			self.num = self.num // 2
			self.stack.append(self.num % 2)
			self.num = self.num // 2
			self.stack.reverse()

s = IntegerToBinary(242)
s.convert()
print (s.stack)
