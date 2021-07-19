# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 21:14:11 2021

@author: gowthas
"""
from collections import deque


class BinaryTreeNode:
    def __init__(self, data=None):
        self._data = data
        self._left = None
        self._right = None

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, data):
        self._data = data
        
    @property
    def left(self):
        return self._left
    
    @left.setter
    def left(self, left):
        self._left = left
        
    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, right):
        self._right = right

    def __repr__(self):
        return "[{} {} {}]".format(self.data, self.left, self.right)
        
    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.data, end=" ")
        if self.right:
            self.right.print_tree()


def create_tree_node_object(pair):
    node = BinaryTreeNode(pair[0])
    if pair[1]:
        node.left = BinaryTreeNode(pair[1])
    if pair[2]:
        node.right = BinaryTreeNode(pair[2])
    return node


def create_tree(parent_child_pair):
    root_node = BinaryTreeNode()
    last_nodes = deque()
    for pair in parent_child_pair:
        if not root_node.data:
            root_node = create_tree_node_object(pair)
            last_nodes.append(root_node.left)
            last_nodes.append(root_node.right)
        else:
            last_node = last_nodes.popleft()
            if not last_node:
                last_node = last_nodes.popleft()
            if pair[1]:
                last_node.left = BinaryTreeNode(pair[1])
                last_nodes.append(last_node.left)
            if pair[2]:
                last_node.right = BinaryTreeNode(pair[2])
                last_nodes.append(last_node.right)
    return root_node


def main():
    binary_tree = BinaryTreeNode()
    binary_tree.data = "headnode"
    print(binary_tree.data)
    parent_child_pair = [[1, 2, 3], [2, 4, 5], [3, 6, 7], [4, 8, 9], [5, 10, 11], [6, 12, 13], [7, 14, 15]]
    tree = create_tree(parent_child_pair)
    tree.print_tree()

    parent_child_pair_missing_node = [[1, 2, 3], [2, 4, None], [3, 6, 7], [4, 8, 9], [6, 12, 13], [7, 14, 15]]
    tree = create_tree(parent_child_pair_missing_node)
    tree.print_tree()


def sample_tree_1():
    parent_child_pair = [[1, 2, 3], [2, 4, 5], [3, 6, 7], [4, 8, 9], [5, 10, 11], [6, 12, 13], [7, 14, 15]]
    tree = create_tree(parent_child_pair)
    return tree


def sample_tree_2():
    parent_child_pair_missing_node = [[1, 2, 3], [2, 4, None], [3, 6, 7], [4, 8, 9], [6, 12, 13], [7, 14, 15]]
    tree = create_tree(parent_child_pair_missing_node)
    return tree


if __name__ == "__main__":
    main()
