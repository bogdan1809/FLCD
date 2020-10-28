from BST import BinarySearchTree


class SymbolTable:
    def __init__(self):
        self.__bst = BinarySearchTree()

    def add(self, value):
        return self.__bst.insert(value)

    def __str__(self):
        return self.__bst.display()

