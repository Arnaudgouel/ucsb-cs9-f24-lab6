class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None
        self.size = 0
    
    def clear(self):
        items_removed = self.size
        self.root = None
        self.size = 0
        return items_removed
    
    def insert(self, item):
        if self.root is None:
            self.root = Node(item)
            self.size += 1
            return 1
        
        current = self.root
        while True:
            if item == current.value:
                return 0
            elif item < current.value:
                if current.left is None:
                    current.left = Node(item)
                    self.size += 1
                    return 1
                current = current.left
            else:
                if current.right is None:
                    current.right = Node(item)
                    self.size += 1
                    return 1
                current = current.right
    
    def _find_max(self, node):
        current = node
        while current.right:
            current = current.right
        return current
    
    def remove(self, item):
        if not self.root:
            return 0
        
        parent = None
        current = self.root
        is_left_child = True
        
        while current and current.value != item:
            parent = current
            if item < current.value:
                current = current.left
                is_left_child = True
            else:
                current = current.right
                is_left_child = False
        
        if not current:  
            return 0
        
        if not current.left and not current.right:
            if current == self.root:
                self.root = None
            elif is_left_child:
                parent.left = None
            else:
                parent.right = None
        
        elif not current.right: 
            if current == self.root:
                self.root = current.left
            elif is_left_child:
                parent.left = current.left
            else:
                parent.right = current.left
        elif not current.left: 
            if current == self.root:
                self.root = current.right
            elif is_left_child:
                parent.left = current.right
            else:
                parent.right = current.right
        
        else:
            predecessor = self._find_max(current.left)
            predecessor_value = predecessor.value
            self.remove(predecessor_value)
            current.value = predecessor_value
            self.size += 1 
        
        self.size -= 1
        return 1
    
    def __len__(self):
        return self.size
    
    def __contains__(self, item):
        current = self.root
        while current:
            if item == current.value:
                return True
            elif item < current.value:
                current = current.left
            else:
                current = current.right
        return False
    
    def _to_string(self, node):
        if node is None:
            return "-"
        if node.left is None and node.right is None:
            return str(node.value)
        return f"({self._to_string(node.left)} {node.value} {self._to_string(node.right)})"
    
    def __str__(self):
        if not self.root:
            return "-"
        return self._to_string(self.root)
    
    def _kth_smallest(self, node, k, count=[0]):
        if not node:
            return None
        
        left_result = self._kth_smallest(node.left, k, count)
        if left_result is not None:
            return left_result
        
        count[0] += 1
        if count[0] == k + 1:
            return node.value
        
        return self._kth_smallest(node.right, k, count)
    
    def __getitem__(self, n):
        if not isinstance(n, int):
            raise TypeError("Index must be an integer")
        
        if n < 0:
            n = len(self) + n
        
        if n < 0 or n >= len(self):
            raise IndexError("Tree index out of range")
        
        result = self._kth_smallest(self.root, n, [0])
        if result is None:
            raise IndexError("Tree index out of range")
        return result