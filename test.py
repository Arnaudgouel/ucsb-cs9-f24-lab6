from tree import Tree

# Create a tree
tree = Tree()

# Insert some values
tree.insert(4)
tree.insert(2)
tree.insert(6)
tree.insert(1)
tree.insert(3)
tree.insert(5)
tree.insert(7)

# Should print: ((1 2 3) 4 (5 6 7))
print(tree)

# Test other operations
print(len(tree))  # Should print: 7
print(3 in tree)  # Should print: True
print(tree[0])    # Should print: 1 (smallest element)
print(tree[-1])   # Should print: 7 (largest element)

tree2 = Tree()

tree2.insert(1)
tree2.insert(2)
tree2.insert(3)

print(tree2)      # Should print: (-)