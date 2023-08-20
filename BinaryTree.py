class TreeNode:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None

# node0 = TreeNode(3)
# node1 = TreeNode(4)
# node2 = TreeNode(5)

# node0.left = node1
# node0.right = node2

# tree = node0

# print(tree.right.key)

tree_tuple = ((1,3,None),2,((None,3,4),5,(6,7,8)))

def parse_tuple(data):
   
    if isinstance(data,tuple) and len(data) == 3:
        node = TreeNode(data[1])
        node.left = parse_tuple(data[0])
        node.right = parse_tuple(data[2])
    elif data is None:
        node = None
    else:
        node =TreeNode(data)
    return node

tree2 = parse_tuple(tree_tuple)

print(tree2.key)

#traversing tree inorder

def traverse_in_order(node):
    if node is None:
        return []
    return(traverse_in_order(node.left) +
           [node.key] + traverse_in_order(node.right))

result = traverse_in_order(tree2)
print(result)
