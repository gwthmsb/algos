
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


def pre_order_recursive(node: BinaryTreeNode, eles):
    if not node:
        return
    if node.data:
        eles.append(node.data)
    pre_order_recursive(node.left, eles)
    pre_order_recursive(node.right, eles)
    return eles


def pre_order_without_recursion(node: BinaryTreeNode):
    result = []
    stack = []
    if not node:
        return result
    if node.data:
        stack.append(node)
    while stack:
        node = stack.pop()
        result.append(node.data)
        if node.right: stack.append(node.right)
        if node.left: stack.append(node.left)
    return result


def in_order_recusrion(node: BinaryTreeNode, eles):
    if not node:
        return eles
    if node.left: in_order_recusrion(node.left, eles)
    if node.data: eles.append(node.data)
    if node.right: in_order_recusrion(node.right, eles)
    return eles


def in_order_without_recursion(node: BinaryTreeNode):
    result = list()
    stack = list()

    if not node:
        return result

    while stack or node:
        if node:
            stack.append(node)
            node = node.left
        else:
            node = stack.pop()
            result.append(node.data)
            node = node.right

    return result


def post_order_recursion(node: BinaryTreeNode, eles):
    if not node:
        return
    if node.left: post_order_recursion(node.left, eles)
    if node.right: post_order_recursion(node.right, eles)
    if node.data: eles.append(node.data)
    return eles


def post_order_without_recursion(node: BinaryTreeNode, eles):
    result = list()
    visited = set()
    if not node:
        return result
    stack = list()

    while stack or node:
        if node:
            stack.append(node)
            node = node.left
        else:
            node = stack.pop()
            if node.right and node.data not in visited:
                stack.append(node)
                node= node.right
            else:
                visited.add(node.data)
                result.append(node.data)
                node = None
    return result


def level_order(node: BinaryTreeNode):
    import queue
    result = []
    q = queue.Queue()
    if node:
        q.put(node)

    while not q.empty():
        node = q.get()
        result.append(node.data)
        if node.left:
            q.put(node.left)
        if node.right:
            q.put(node.right)

    return result

def main():
    # print("pre_order_recursive : {}".format(pre_order_recursive(sample_tree_1(), list())))
    # print("pre_order_without_recursion : {}".format(pre_order_without_recursion(sample_tree_1())))
    # print("in_order_recusrion : {}".format(in_order_recusrion(sample_tree_1(), list())))
    # print("in_order_without_recursion : {}".format(in_order_without_recursion(sample_tree_1())))
    # print("post_order_recursion : {}".format(post_order_recursion(sample_tree_1(), list())))
    # print("post_order_without_recursion: {}".format(post_order_without_recursion(sample_tree_1(), list())))
    print("Level order traversing: {}".format(level_order(sample_tree_1())))


if __name__ == "__main__":
    main()