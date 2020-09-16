from stackdatastructure import Stack


def is_paren_balanced(paren_string):
	index = 0
	while index < len(paren_string):
		paren_string = list(paren_string)
		paren = paren_string[index]
		other = paren_string.pop()
		
		if paren == other:
			print ("Yes")
			index += 1



is_paren_balanced("(({()}))")