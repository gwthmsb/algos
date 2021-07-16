
from trees.binary_tree import BinaryTreeNode, sample_tree_1
from copy import deepcopy
"""
Finding max in a tree

"""

max = float("-infinity")
def find_max_in_tree(tree_for_max):
    global max
    if tree_for_max:
        if tree_for_max.data > max:
            max = tree_for_max.data
        find_max_in_tree(tree_for_max.left)
        find_max_in_tree(tree_for_max.right)
    return max


def main():
    tree = sample_tree_1()
    print(tree)
    print("Max in given tree is: {}".format(find_max_in_tree(tree)))


if __name__=="__main__":
    main()

