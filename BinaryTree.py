class TreeNode:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None

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


def preorderTraversal(node):
    if node is None:
        return []
    return ([node.key] + preorderTraversal(node.left) + preorderTraversal(node.right))
    
def postorderTraversal(node):
    if node is None:
        return []
    return (postorderTraversal(node.left) + postorderTraversal(node.right) + [node.key])

result = postorderTraversal(tree2)
print(result)
