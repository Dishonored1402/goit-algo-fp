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
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def to_list(self):
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def sorted_merge(self, other):
        dummy = Node(0)
        tail = dummy

        a, b = self.head, other.head

        while a and b:
            if a.data <= b.data:
                tail.next = a
                a = a.next
            else:
                tail.next = b
                b = b.next
            tail = tail.next

        tail.next = a if a else b
        self.head = dummy.next

    def insertion_sort(self):
        sorted_list = None
        current = self.head

        while current:
            next_node = current.next
            if sorted_list is None or current.data < sorted_list.data:
                current.next = sorted_list
                sorted_list = current
            else:
                temp = sorted_list
                while temp.next and temp.next.data < current.data:
                    temp = temp.next
                current.next = temp.next
                temp.next = current
            current = next_node

        self.head = sorted_list

list1 = LinkedList()
list1.append(3)
list1.append(1)
list1.append(4)
list1.append(2)

print("Оригінальний список:", list1.to_list())
list1.reverse()
print("Перевернутий список:", list1.to_list())

list1.insertion_sort()
print("Відсортований список:", list1.to_list())

list2 = LinkedList()
list2.append(5)
list2.append(6)
list2.append(7)

list1.sorted_merge(list2)
print("Об'єднаний список:", list1.to_list())
