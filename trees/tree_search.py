
from trees.binary_tree import BinaryTreeNode, sample_tree_1, sample_tree_2
from copy import deepcopy
from queue import Queue
"""
Finding max in a tree

"""

max = float("-infinity")
def find_max_in_tree(tree_for_max: BinaryTreeNode) -> float:
    global max
    if tree_for_max:
        if tree_for_max.data > max:
            max = tree_for_max.data
        find_max_in_tree(tree_for_max.left)
        find_max_in_tree(tree_for_max.right)
    return max


def find_max_in_tree_not_recursion(tree_for_max: BinaryTreeNode) -> float:
    max_element = float("-infinity")
    if not tree_for_max:
        return max_element

    queue = Queue()
    queue.put(tree_for_max)
    while not queue.empty():
        node = queue.get()
        if max_element < node.data:
            max_element = node.data
        if node.left:
            queue.put(node.left)
        if node.right:
            queue.put(node.right)
    return max_element


def search_in_tree(tree_root: BinaryTreeNode, ele_to_search) -> bool:
    if not tree_root:
        return False
    queue = Queue()
    queue.put(tree_root)
    while not queue.empty():
        node = queue.get()
        if ele_to_search == node.data:
            return True
        if node.left:
            queue.put(node.left)
        if node.right:
            queue.put(node.right)
    return False


def size_of_binary_tree(tree_root: BinaryTreeNode) -> int:
    size = 0

    if tree_root:
        queue = Queue()
        queue.put(tree_root)
        while not queue.empty():
            node = queue.get()
            size = size+1
            if node.left:
                queue.put(node.left)
            if node.right:
                queue.put(node.right)
    return size


def level_order_in_reverse(tree_root: BinaryTreeNode):
    result = []
    if tree_root:
        queue = Queue()
        queue.put(tree_root)
        while not queue.empty():
            node = queue.get()
            if node.left:
                queue.put(node.left)
            if node.right:
                queue.put(node.right)
            result.append(node.data)
    result.reverse()
    return result

def main():
    tree = sample_tree_1()
    print(tree)
    print("Max in given tree is: {}".format(find_max_in_tree(tree)))
    print("Max in given tree is(without recursion): {}".format(find_max_in_tree_not_recursion(tree)))
    print(search_in_tree(tree, 15))
    print(search_in_tree(tree, 16))
    print(size_of_binary_tree(tree))
    print(size_of_binary_tree(sample_tree_2()))
    print(level_order_in_reverse(sample_tree_1()))


if __name__ == "__main__":
    main()

