from BST import BinarySearchTree
class SymbolTable:
    def __init__(self):
        self.__bst = BinarySearchTree()

    def add(self,value):
        self.__bst.insert(value)

