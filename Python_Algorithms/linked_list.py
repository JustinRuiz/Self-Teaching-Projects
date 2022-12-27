
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def prepend(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def pop(self):
        
        if self.head == self.tail:
            return None
        
        temp = self.head
        pre = self.head

        while(temp.next):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp.value


my_linked_list = LinkList(4)

my_linked_list.append(10)
my_linked_list.append(20)
print(my_linked_list.pop())

print(my_linked_list.head.value)
print(my_linked_list.tail.value)

my_linked_list.prepend(5)

print(my_linked_list.head.value)
print(my_linked_list.head.next.value)