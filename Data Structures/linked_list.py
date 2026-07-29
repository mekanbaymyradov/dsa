

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return

        ll_str = ""
        curr = self.head
        while curr:
            ll_str += str(curr.data) + "->"
            curr = curr.next

        print(ll_str)

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        curr = self.head
        while curr.next:
            curr = curr.next

        curr.next = Node(data, None)

    def get_length(self):
        count = 0
        curr = self.head
        while curr:
            curr = curr.next
            count += 1
            
        return count

    def remove_at(self, index):
        if index < 0 or self.head is None:
            raise IndexError("Index out of range")

        if index == 0:
            self.head = self.head.next
            return

        curr = self.head
        for _ in range(index - 1):
            if curr.next is None:
                raise IndexError("Index out of range")
            curr = curr.next
            
        if curr.next is None:
            raise IndexError("Index out of range")

        curr.next = curr.next.next

    def insert_at(self, index, data):
        if index < 0:
            raise IndexError("Index out of range")

        if index == 0:
            self.insert_at_beginning(data)
            return
        
        count = 0    
        curr = self.head
        while curr:
            if count == index - 1:
                node = Node(data, curr.next)
                curr.next = node
                return
                
            curr = curr.next
            count += 1
            
        raise IndexError("Index out of range")

    def insert_after_value(self, data_after, data_to_insert):
        if self.head is None:
            raise ValueError("Linked list is empty")
            
        curr = self.head

        while curr:
            if curr.data == data_after:
                node = Node(data_to_insert, curr.next)
                curr.next = node
                return
            curr = curr.next

        raise ValueError("Given data not found")
        
        

if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_at_beginning("apple")
    ll.insert_at_beginning("orange")
    ll.insert_at_end("banana")
    ll.print()
    print("length:", ll.get_length())
    ll.remove_at(1)
    ll.insert_at(1, "grapes")
    ll.insert_after_value("orange","mango")
    ll.insert_after_value("mango","apple")
    ll.print()