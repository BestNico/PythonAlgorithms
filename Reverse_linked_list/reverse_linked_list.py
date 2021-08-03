from dataclasses import dataclass

@dataclass
class Node:
    """ Linked list node """
    value: int
    next: object = None


# init linked list
fifth_node = Node(value=5, next=None)
forth_node = Node(value=4, next=fifth_node)
third_node = Node(value=3, next=forth_node)
second_node = Node(value=2, next=third_node)
head_node = first_node = Node(value=1, next=second_node)

# iterator

def reverse_on_iterator(head: Node) -> Node:
    """ reverse_on_iterator """
    pre = None
    curr = head

    while curr != None:
        next = curr.next
        curr.next = pre
        pre = curr
        curr = next
    
    return pre


print(reverse_on_iterator(head_node))



