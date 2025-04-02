#1825622
#Prince Edwin Nyarko

# Node class for the binary tree
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Function to check if a tree is a valid BST
def is_valid_bst(root, min_val=float('-inf'), max_val=float('inf')):
    if not root:
        return True
    if not (min_val < root.val < max_val):
        return False
    return (is_valid_bst(root.left, min_val, root.val) and
            is_valid_bst(root.right, root.val, max_val))

# In-order traversal to print elements in sorted order
def in_order_traversal(root):
    if root:
        in_order_traversal(root.left)
        print(root.val, end=" ")
        in_order_traversal(root.right)

# Max-Heap Implementation
class MaxHeap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) // 2

    def left_child(self, i):
        return 2 * i + 1

    def right_child(self, i):
        return 2 * i + 2

    def insert(self, val):
        """ Inserts an element into the max-heap """
        self.heap.append(val)
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, index):
        """ Moves the element up to maintain max-heap property """
        while index > 0 and self.heap[self.parent(index)] < self.heap[index]:
            self.heap[self.parent(index)], self.heap[index] = self.heap[index], self.heap[self.parent(index)]
            index = self.parent(index)

    def extract_max(self):
        """ Extracts the max element (root) from the heap """
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        
        root = self.heap[0]
        self.heap[0] = self.heap.pop()  
        self._heapify_down(0) 
        return root

    def _heapify_down(self, index):
        """ Moves the element down to maintain max-heap property """
        largest = index
        left = self.left_child(index)
        right = self.right_child(index)

        if left < len(self.heap) and self.heap[left] > self.heap[largest]:
            largest = left
        if right < len(self.heap) and self.heap[right] > self.heap[largest]:
            largest = right
        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self._heapify_down(largest)

# Function to build a max-heap from an unsorted array
def build_max_heap(arr):
    max_heap = MaxHeap()
    for num in arr:
        max_heap.insert(num)
    return max_heap

# Function to return top-K elements from a max-heap
def get_top_k_elements(arr, k):
    if k <= 0:
        return []
    
    max_heap = build_max_heap(arr)
    top_k = [max_heap.extract_max() for _ in range(min(k, len(arr)))]
    return top_k

# Example Usage
if __name__ == "__main__":
    # Example Binary Tree
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(7)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(8)

    # Check if it's a valid BST
    print("Is valid BST:", is_valid_bst(root))

    # Print elements in sorted order
    print("Elements in sorted order:")
    in_order_traversal(root)
    print()

    # Example array for max-heap
    arr = [10, 20, 15, 30, 40]
    k = 3
    print(f"Top-{k} elements from max-heap:", get_top_k_elements(arr, k))
