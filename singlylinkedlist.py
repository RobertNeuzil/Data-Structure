class Node:
    def __init__(self, data = None, next_n = None):
        self.data = data
        self.next_n = next_n


class LinkedList:
    def __init__(self, head = None):
        self.head = head

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next_n:
            last_node = last_node.next_n
        last_node.next_n = new_node

    def print(self):
        cur_node = self.head
        while cur_node:
            print (cur_node.data)
            cur_node = cur_node.next_n

    def prepend(self, data):
        new_node = Node(data)
        cur_node = self.head
        new_node.next_n = cur_node
        self.head = new_node

    def insert_after_node (self, data, key):
        cur_node = self.head
        new_node = Node(data)
        
        if key is cur_node.data:
            new_node.next_n = cur_node.next_n
            cur_node.next_n = new_node
            return
        while cur_node.data is not key:
            prev_node = cur_node
            cur_node = cur_node.next_n
        
        new_node.next_n = cur_node.next_n
        cur_node.next_n = new_node

    def delete_from_list(self, delete):
        cur_node = self.head

        if cur_node.data is delete:
            self.head = cur_node.next_n
            cur_node = None
            return

        while cur_node.data is not delete:
            prev_node = cur_node
            cur_node = cur_node.next_n

        prev_node.next_n = cur_node.next_n
        cur_node.data = None


    def delete_at_position(self, pos):
        cur_node = self.head
        count = 0
        if pos == 0:
            self.head = cur_node.next_n
            cur_node.data = None
            return
        while count != pos:
            count += 1
            prev_node = cur_node
            cur_node = cur_node.next_n

        prev_node.next_n = cur_node.next_n
        cur_node.data = None

    def node_swap(self, key1, key2): #swap key1 and key2

        if key1 == key2:
            print ("Disqualifying")
            return False

        prev_1 = None
        cur_node = self.head

        while cur_node and cur_node.data != key1:
            prev_1 = cur_node
            cur_node = cur_node.next_n

        prev_2 = None
        curr_2 = self.head
        while curr_2 and curr_2.data != key2:
            prev_2 = curr_2
            curr_2 = curr_2.next_n

        if not cur_node or not curr_2:
            print ("Disqualifying")
            return False

        if prev_1:
            prev_1.next_n = curr_2
        else:
            self.head = curr_2
        if prev_2:
            prev_2.next_n = cur_node
        else:
            self.head = cur_node

        cur_node.next_n, curr_2.next_n = curr_2.next_n, cur_node.next_n



        
llist = LinkedList()
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")
llist.node_swap("B", 'C')
llist.print()















'''

s = LinkedList()
s.append(10)
s.append(20)
s.append(30)
s.prepend(3423)
s.append(40)
s.append(50)
s.append(60)
s.delete_at_position(4)
s.insert_after_node(13, 30)
s.delete_from_list(10)
s.print()


'''
