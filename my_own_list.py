class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")

    def __iter__(self):
        # self.iter_node = self.head 
        # return self
        return node_gen(self.head)
        # return LinkedListGen(self.head)
    
    # def __next__(self):
    #     if self.iter_node:
    #         ret = self.iter_node.data
    #         self.iter_node = self.iter_node.next
    #         return ret

def node_gen(node:Node|None):
    while node:
        yield node.data
        node = node.next
    
class LinkedListGen:
    def __init__(self, node:Node|None) -> None:
        self.node = node

    def __iter__(self):
        return self

    def __next__(self):
        if self.node:
            ret = self.node.data
            self.node = self.node.next
            return ret
        raise StopIteration

# Användning
linked_list = LinkedList()
linked_list.append('a')
linked_list.append('b')
linked_list.append('c')
linked_list.append('d')
linked_list.append('e')
linked_list.print_list()  # Output: 1 -> 2 -> 3 -> None

print(type(iter(linked_list)))
# for node_data in linked_list:
#     print(node_data)


for data in linked_list:
    #print(data, end='')
    # input()
    for i in linked_list:
        print(f'{data}:{i}')