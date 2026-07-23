from typing import Any

class Node:
    def __init__(self, data: Any, next=None) -> None:
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def insert_at_beginning(self, data: Any) -> None:
        node = Node(data, self.head)

        self.head = node

    def insert_at_end(self, data: Any) -> None:
        if not self.head:
            self.head = Node(data)
            return
            
        curr = self.head
        while curr.next:
            curr = curr.next

        curr.next = Node(data)

    def print(self) -> None:
        if self.head is None:
            print("Linked list is empty")
            return

        curr = self.head
        ll_str = ""
        while curr:
            ll_str += f"{curr.data}->"
            curr = curr.next
            
        print(ll_str)

    def insert_values(self, data_list: list) -> None:
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self) -> int:
        count = 0
        curr = self.head

        while curr:
            count += 1
            curr = curr.next
            
        return count

    def remove_at(self, index: int) -> None:
        if index < 0 or index >= self.get_length() or not self.head:
            raise Exception("Invalid index")

        if index == 0:
            self.head = self.head.next
            return

        curr = self.head
        count = 0
        while curr and curr.next:
            if count == index - 1:
                curr.next = curr.next.next
                return
            curr = curr.next
            count += 1

    def insert_at(self, index: int, data: Any) -> None:
        if index < 0 or index > self.get_length():
            raise Exception("Invalid index")
            
        if index == 0:
            self.insert_at_beginning(data)
            return

        curr = self.head
        count = 0
        while curr:
            if count == index - 1:
                node = Node(data, curr.next)
                curr.next = node
                return
                
            curr = curr.next
            count += 1
        
        
        


if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_values(["apple", "banana", "orange"])
    ll.print()
    print("length of linked list:", ll.get_length())
    ll.remove_at(1)
    ll.insert_at(0, "mango")
    ll.insert_at(3, "grapes")
    ll.insert_at(3, "figs")
    ll.print()
    
            
        