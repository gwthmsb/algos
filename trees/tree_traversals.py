
from trees.binary_tree import BinaryTreeNode, sample_tree_1, sample_tree_2

"""
Traversing tree
D - Visiting the node
L - Visiting the left subtree
R - Visiting the right subtree

Pre-order traversal: DLR
In-order traversal: LDR
Post-order traversal: LRD
Lever-order traversal(Breadth first traversal)

"""

eles = list()
def pre_order_recursive(node: BinaryTreeNode):
    if not node:
        return
    if node.data:
        eles.append(node.data)
    eles.append(pre_order_recursive(node.left))
    eles.append(pre_order_recursive(node.right))
    return eles

print(pre_order_recursive(sample_tree_1()))
