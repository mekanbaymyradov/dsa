
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, val):
        node = Node(val, self.head)
        self.head = node

    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return

        ll_str = ""
        curr = self.head
        while curr:
            ll_str += str(curr.val) + "->"
            curr = curr.next

        print(ll_str)

    def insert_at_end(self, val):
        if self.head is None:
            self.head = Node(val, None)
            return

        curr = self.head
        while curr.next:
            curr = curr.next

        curr.next = Node(val, None)

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

    def insert_at(self, index, val):
        if index < 0:
            raise IndexError("Index out of range")

        if index == 0:
            self.insert_at_beginning(val)
            return
        
        count = 0    
        curr = self.head
        while curr:
            if count == index - 1:
                node = Node(val, curr.next)
                curr.next = node
                return
                
            curr = curr.next
            count += 1
            
        raise IndexError("Index out of range")

    def insert_after_value(self, val_after, val_to_insert):            
        curr = self.head

        while curr:
            if curr.val == val_after:
                node = Node(val_to_insert, curr.next)
                curr.next = node
                return
            curr = curr.next

        raise ValueError("Given val not found")

    def remove_by_value(self, val):
        if self.head is None:
            raise ValueError("Given val not found")
            
        if self.head.val == val:
            self.head = self.head.next
            return

        curr = self.head
        while curr.next:
            if curr.next.val == val:
                curr.next = curr.next.next
                return
                
            curr = curr.next
            
        raise ValueError("Given val not found")

    def insert_nodes(self, values):
        if not values:
            self.head = None
            return
            
        self.head = Node(values[0], None)
        curr = self.head

        for val in values[1:]:
            curr.next = Node(val, None)
            curr = curr.next

    @classmethod
    def from_head(cls, head):
        ll = cls()
        ll.head = head
        return ll

    @classmethod
    def from_list(cls, values):
        ll = cls()
        ll.insert_nodes(values)
        return ll
        

if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_at_beginning("apple")
    ll.insert_at_beginning("orange")
    ll.insert_at_end("banana")
    ll.remove_at(1)
    ll.insert_at(1, "grapes")
    ll.insert_after_value("orange","mango")
    ll.insert_after_value("mango","apple")
    print("length:", ll.get_length())
    ll.print()
    ll.remove_by_value("mango")
    ll.print()