from PIF import ProgramInternalForm
from scanner import get_tokens, isConstant, isIdentifier
from SymbolTable import SymbolTable
from tokenList import *

if __name__ == '__main__':
    file_name = input("Input the name of the program you want to run: ")

    file = open(file_name, 'r')
    for line in file:
        print(line)

    symbol_table = SymbolTable()
    pif = ProgramInternalForm()
    with open(file_name, 'r') as file:
        line_nr = 0
        for line in file:

            line_nr += 1
            tokenList = get_tokens(line, separators)
            print(tokenList)
            for token in tokenList:
                if token in allTokens:
                    pif.add(token, -1)
                elif isIdentifier(token):
                    id = symbol_table.add(token)
                    pif.add("identifier", id)
                elif isConstant(token):
                    id = symbol_table.add(token)
                else:
                    raise Exception("Unknown token " + token + " at line" + str(line_nr))

    print("PIF:\n", pif)
    print("ST:\n", symbol_table)
