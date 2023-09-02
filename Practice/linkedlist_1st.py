class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self): 
        current = self 
        values = []
        while current is not None:
            values.append(str(current.value))
            current = current.next
        return " -> ".join(values) + " -> None"

    def reverse_linked_list(self):
        prev = None
        current = self

        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev

# Creating a sample linked list: 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

print("Original linked list:")
print(head)

reversed_head = head.reverse_linked_list()
print("\nReversed linked list:")
print(reversed_head)
