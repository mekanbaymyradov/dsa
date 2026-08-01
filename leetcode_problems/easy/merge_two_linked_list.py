from data_structures.linked_list import LinkedList, Node


class Solution:
    def mergeTwoLists(self, list1: Node | None, list2: Node | None) -> Node | None:
        
        dummy = Node()

        curr = dummy

        while list1 and list2:
            if list1.val > list2.val:
                curr.next = list2
                list2 = list2.next
            else:
                curr.next = list1
                list1 = list1.next
            
            curr = curr.next

        if list1:
            curr.next = list1
        elif list2:
            curr.next = list2

        return dummy.next

if __name__ == "__main__":
    ll1 = LinkedList.from_list([1, 2, 3])
    ll2 = LinkedList.from_list([1, 2, 3, 4, 5])

    solution = Solution()
    LinkedList.from_head(solution.mergeTwoLists(ll1.head, ll2.head)).print()