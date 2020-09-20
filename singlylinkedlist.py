class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node

    def insert_after_node(self, prev_node, data):

        if not prev_node:
            print("Previous node is not in the list")
            return 

        new_node = Node(data)

        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key):

        cur_node = self.head

        if cur_node and cur_node.data == key:
            self.head = cur_node.next
            cur_node = None
            return

        prev = None 
        while cur_node and cur_node.data != key:
            prev = cur_node
            cur_node = cur_node.next

        if cur_node is None:
            return 

        prev.next = cur_node.next
        cur_node = None

    def delete_node_at_pos(self, pos):

        cur_node = self.head

        if pos == 0:
            self.head = cur_node.next
            cur_node = None
            return

        prev = None
        count = 1
        while cur_node and count != pos:
            prev = cur_node 
            cur_node = cur_node.next
            count += 1

        if cur_node is None:
            return 

        prev.next = cur_node.next
        cur_node = None

    def len_iterative(self):

        count = 0
        cur_node = self.head

        while cur_node:
            count += 1
            cur_node = cur_node.next
        return count

    def len_recursive(self, node):
        if node is None:
            return 0
        return 1 + self.len_recursive(node.next)

    def swap_nodes(self, key1, key2):
        prev_node = None
        cur_node = self.head
        prev_node_2 = None
        cur_node_2 = self.head

        if key1 == key2:
            return
        


        while cur_node and cur_node.data != key1:
            prev_node = cur_node
            cur_node = cur_node.next
        while cur_node_2.data != key2:
            prev_node_2 = cur_node_2
            cur_node_2 = cur_node_2.next
            
        if prev_node == None or prev_node_2 == None:
            cur_node.next = cur_node_2.next  # 1 > 3
            cur_node_2.next = cur_node  # 2 > 1
            self.head = cur_node_2
            return

        # 1 > 2 > 3 > 4

        #1 > 2
        #2 > 3
        
        prev_node.next = cur_node_2 # 1 > 3
        cur_node.next = cur_node_2.next # 2 > 4
        cur_node_2.next = cur_node # 3 > 2


    def reverse_iterative(self):
        #A>B>C>D      D>C>B>A

        prev_node = None 
        cur_node = self.head
        
        while cur_node:
            nxt = cur_node.next
            cur_node.next = prev_node
            prev_node = cur_node
            cur_node = nxt

        self.head = prev_node     # At end of loop, prev node is last node and cur node has been assigned None









    def reverse_recursive(self):

        def _reverse_recursive(cur, prev):
            if not cur:
                return prev

            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
            return _reverse_recursive(cur, prev)

        self.head = _reverse_recursive(cur= self.head, prev = None)



    def merge_two_sorted(self, second_list):
        p = self.head
        q = second_list.head

        if not p:
            return q
        if not q:
            return p

        if p and q:
            pass




llist = LinkedList()

llist.append(1)
llist.append(3)
llist.append(5)
llist.append(7)
llist.append(8)
llist.append(10)

second_list = LinkedList()

second_list.append(2)
second_list.append(4)
second_list.append(6)
second_list.append(8)
second_list.append(9)
second_list.append(11)

llist.merge_two_sorted(second_list)





'''


llist = LinkedList()
llist.append(1)
llist.append(2)
llist.append(3)
llist.append(4)

'''


'''
        
llist = LinkedList()
llist.append(1)
llist.append(2)
llist.append(3)
llist.append(4)
llist.swap_nodes(1, 2)
llist.print_list()
llist.reverse_iterative()
llist.reverse_recursive()




#llist.reverse_iterative()

'''

llist.print_list()
