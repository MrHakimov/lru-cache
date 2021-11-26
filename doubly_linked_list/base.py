class Node:
    def __init__(self, key, value, _prev: "Node" = None, _next: "Node" = None):
        self.key = key
        self.value = value
        self.prev = _prev
        self.next = _next

    def __eq__(self, other):
        return self.key == other.key and self.value == other.value


class DoublyLinkedList:
    def __init__(self):
        self.dummy_head = Node(0, 0)
        self.tail = self.dummy_head

        self.size = 0

    def get_head(self) -> Node:
        assert not self.is_empty()

        return self.dummy_head.next

    def get_tail(self) -> Node:
        assert not self.is_empty()

        return self.tail

    def __len__(self) -> int:
        return self.size

    def put_left(self, key, value) -> Node:
        head = self.dummy_head.next
        node = Node(key, value, _prev=self.dummy_head, _next=head)

        if head is not None:
            head.prev = node
        else:
            self.tail = node
            self.tail.prev = self.dummy_head

        self.dummy_head.next = node

        self.size += 1

        return node

    def put_right(self, key, value) -> Node:
        node = Node(key, value, _prev=self.tail)
        self.tail.next = node
        self.tail = node

        self.size += 1

        return node

    def is_empty(self) -> bool:
        return len(self) == 0

    def pop_left(self) -> Node:
        assert not self.is_empty()

        return_node = self.dummy_head.next

        next_next = self.dummy_head.next.next
        self.dummy_head.next = next_next
        if next_next is not None:
            next_next.prev = self.dummy_head

        # there would be no nodes referencing to the removing node
        # and it would be deallocated by Python's GC

        self.size -= 1

        return return_node

    def pop_right(self) -> Node:
        assert not self.is_empty()

        return_node = self.tail

        prev = self.tail.prev
        prev.next = None
        self.tail = prev

        self.size -= 1

        return return_node

    def delete_node(self, node: Node):
        assert node is not None
        assert not self.is_empty()

        _prev = node.prev
        _next = node.next
        _prev.next = _next
        if _next is not None:
            _next.prev = _prev
        else:
            self.tail = _prev

        self.size -= 1
