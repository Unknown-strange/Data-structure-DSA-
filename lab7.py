#1825622
# Binary Search Implementation
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Example usage for binary search
arr = [1, 3, 5, 7, 9]
target = 5
print(f"Index of {target}:", binary_search(arr, target))  # Output: 2

def find_first(arr, target):
    left = 0
    right = len(arr) - 1
    first = -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            first = mid
            right = mid - 1  # Look for earlier occurrences
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return first

# Example usage for finding first occurrence
arr = [1, 2, 2, 2, 3]
target = 2
print(f"First occurrence of {target}:", find_first(arr, target))  # Output: 1


# Basic Trie Implementation
class TrieNode:
    def _init_(self):
        self.children = {}
        self.is_end = False

class Trie:
    def _init_(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end

# Example usage for Trie
trie = Trie()
words = ["apple", "app", "banana"]
for word in words:
    trie.insert(word)

print("Search 'app':", trie.search("app"))   # Output: True
print("Search 'appl':", trie.search("appl")) # Output: False


# Ternary Search Tree Implementation
class TSTNode:
    def _init_(self, char):
        self.char = char
        self.left = None
        self.middle = None
        self.right = None
        self.is_end = False

class TernarySearchTree:
    def _init_(self):
        self.root = None

    def insert(self, word):
        self.root = self._insert(self.root, word, 0)

    def _insert(self, node, word, index):
        if index >= len(word):
            return node
        char = word[index]
        if node is None:
            node = TSTNode(char)
        if char < node.char:
            node.left = self._insert(node.left, word, index)
        elif char > node.char:
            node.right = self._insert(node.right, word, index)
        else:
            if index == len(word) - 1:
                node.is_end = True
            else:
                node.middle = self._insert(node.middle, word, index + 1)
        return node

    def search(self, word):
        return self._search(self.root, word, 0)

    def _search(self, node, word, index):
        if index >= len(word) or node is None:
            return False
        char = word[index]
        if char < node.char:
            return self._search(node.left, word, index)
        elif char > node.char:
            return self._search(node.right, word, index)
        else:
            if index == len(word) - 1:
                return node.is_end
            else:
                return self._search(node.middle, word, index + 1)

# Example usage for TST
tst = TernarySearchTree()
words = ["cat", "car", "bus"]
for word in words:
    tst.insert(word)

print("Search 'cat':", tst.search("cat"))  # Output: True
print("Search 'car':", tst.search("car"))  # Output: True
print("Search 'ca':", tst.search("ca"))   # Output: False
print("Search 'bus':", tst.search("bus")) # Output: True