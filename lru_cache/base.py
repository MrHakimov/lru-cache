import typing
from doubly_linked_list import Node, DoublyLinkedList


class LRUCache:
    def __init__(self, capacity: int):
        assert capacity > 0

        self.capacity = capacity
        self.nodes = DoublyLinkedList()
        self.key_to_node: dict[typing.Any, Node] = dict()

    def __len__(self) -> int:
        return len(self.nodes)

    def is_empty(self) -> bool:
        return len(self) == 0

    def __move_to_front(self, key, node: Node):
        self.nodes.delete_node(node)
        new_node = self.nodes.put_left(key, node.value)
        self.key_to_node[key] = new_node

    def get(self, key) -> typing.Optional:
        node = self.key_to_node.get(key, None)

        if node is None:
            return None

        self.__move_to_front(key, node)

        return node.value

    def put(self, key, value):
        if len(self.nodes) == self.capacity:
            removed_node = self.nodes.pop_right()
            self.key_to_node.pop(removed_node.key)

        assert 0 <= len(self.nodes) < self.capacity

        node = self.key_to_node.get(key, None)
        if node is not None:
            node.value = value
            self.__move_to_front(key, node)

            return

        node = self.nodes.put_left(key, value)
        self.key_to_node[key] = node
