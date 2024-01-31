from enum import Enum, auto
from typing import Self
from collections import deque
import time

NODES_TO_INSERT = 101  # It's nice to have this be an odd number, then it can be balanced if you choose a mid 
                       # node to be the root

class Balance(Enum):
    LEFT_HEAVY = auto()
    BALANCED = auto()
    RIGHT_HEAVY = auto()

class Node:
    def __init__(self, value: int) -> None:
        self.value = value
        self.left: Self | None = None # I miss Rust's Option<T> type :(
        self.right: Self | None = None

    @property
    def height(self) -> int: return max(self._height(self.left), self._height(self.right))
    def _height(self, node: Self | None) -> int:
        if node is None: return 0
        return 1 + max(self._height(node.left), self._height(node.right))
    
    @property
    def balance_factor(self) -> int: return self._height(self.left) - self._height(self.right)
    @property
    def balance_factor_type(self) -> Balance: 
        if self.balance_factor > 1: return Balance.LEFT_HEAVY
        if self.balance_factor < -1: return Balance.RIGHT_HEAVY
        return Balance.BALANCED

    def __repr__(self) -> str: return f"Node({self.value})"

class Tree:
    def __init__(self, root: Node) -> None:
        self.root = root
        self.height = root.height

    def insert(self, node: Node) -> bool: return self._insert(node, self.root)
    def _insert(self, node: Node, current: Node) -> bool:
        if node.value < current.value:
            if current.left is None:
                current.left = node
                return True
            return self._insert(node, current.left)
        if node.value > current.value:
            if current.right is None:
                current.right = node
                return True
            return self._insert(node, current.right)
        return False  # This happens if you try to insert a duplicate value

    # Searching the tree, this is a DFS search
    def search(self, needle: Node) -> bool: return self._search(needle, self.root)
    def _search(self, needle: Node, haystack: Node | None) -> bool:
        if haystack is None: return False
        if haystack.value > needle.value: return self._search(needle, haystack.left)
        if haystack.value < needle.value: return self._search(needle, haystack.right)
        return True

    @property
    def size(self) -> int: return self._size(self.root)
    def _size(self, node: Node | None) -> int:
        if node is None: return 0
        return 1 + self._size(node.left) + self._size(node.right) 

    # Pre-order traversal of the tree
    def preorder(self) -> list[Node]:
        order: list[Node] = []
        self._preorder(self.root, order)
        return order
    def _preorder(self, node: Node | None, order: list[Node]) -> None:
        if node is None: return
        order.append(node)
        self._preorder(node.left, order)
        self._preorder(node.right, order)

    # In-order traversal of the tree
    def inorder(self) -> list[Node]:
        order: list[Node] = []
        self._inorder(self.root, order)
        return order
    def _inorder(self, node: Node | None, order: list[Node]) -> None:
        if node is None: return
        self._inorder(node.left, order)
        order.append(node)
        self._inorder(node.right, order)

    # Post-order traversal of the tree
    def postorder(self) -> list[Node]:
        order: list[Node] = []
        self._postorder(self.root, order)
        return order
    def _postorder(self, node: Node | None, order: list[Node]) -> None:
        if node is None: return
        self._postorder(node.left, order)
        self._postorder(node.right, order)
        order.append(node)

    # Level-order traversal of the tree (breadth-first search)
    def levelorder(self) -> list[Node]:
        order, q = [], deque([self.root])

        while len(q):
            cur = q.popleft() # since we can pass an index, a list can act as a queue, no imports!
            order.append(cur)
            if cur.left: q.append(cur.left)
            if cur.right: q.append(cur.right)
        return order

if __name__ == "__main__":
    import random

    # Generate NODES_TO_INSERT unique values, sort them and select midpoint for a balanced tree
    # and ensure we have a good range to choose nodes from
    vals = random.sample(range(1, NODES_TO_INSERT * 10), NODES_TO_INSERT)
    # vals = sorted(random.sample(range(1, NODES_TO_INSERT * 10), NODES_TO_INSERT))

    # Side note, unique? dumb? way to generate N unique random numbers as long
    # as we have some sort of Set structure (there is a possibly could run for a bit more 
    # than N iterations:
    # ```
    # vals: set[int] = set()
    # while len(vals) != N: vals.add(random.randrange(1, 100))
    # ```

    # Construct the tree. Take the middle value of the sorted list to create the most balanced tree
    # midpoint = len(vals) // 2
    # root = Node(vals.pop(midpoint))
    root = Node(vals.pop(0)) # change pop argument to midpoint for a balanced tree (as long as NODES_TO_INSERT is odd. (?))
                             # or 0 for the random structure
    tree = Tree(root)

    # Append nodes to the tree
    start = time.time()
    for val in vals: out = tree.insert(Node(val))
    print(f"insertion took {time.time() - start:.6f}s")
    assert tree.size == NODES_TO_INSERT, "The size of the tree is not correct"

    # Information about the tree
    # print(f"{tree.root.balance_factor_type = }")
    # print(f"{tree.preorder() = }")
    # print(f"{tree.inorder() = }")
    # print(f"{tree.postorder() = }")
    # print(f"{tree.levelorder() = }")

    # Ensure we can search and find everything
    found = True
    start = time.time()
    for val in vals: found &= tree.search(Node(val))
    print(f"search took {time.time() - start:.6f}s")
    assert found, "Search is broken"

    # Ensure if we try to duplicate any search it always comes back False
    inserted = False
    start = time.time()
    for val in vals: inserted |= tree.insert(Node(val))
    print(f"dup insertion took {time.time() - start:.6f}s")
    assert not inserted, "Something was inserted that shouldn't have been."
