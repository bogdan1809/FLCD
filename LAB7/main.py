from FiniteAutomata import *
from Grammar import *
from Parser import Parser

if __name__ == '__main__':
    fa = FiniteAutomata()
    fa.readFile("fa.txt")
    opt = 100
    opt2 = 100
    while opt != 0:
        print("1-Print states,alphabet,transitions and final states")
        print("2-Verify if FA is deterministic")
        print("3-Enter sequence and see if accepted")
        print("4-Read grammar")
        print("5-Parser")
        opt = int(input("Pick one"))
        if opt == 1:
            fa.printAll()
        elif opt == 2:
            print(fa.checkIfDeterministic())
        elif opt == 3:
            seq = str(input("enter sequence: "))
            print(fa.isAccepted(seq))
        elif opt == 4:
            while opt2 != 0:
                grammar = Grammar("grammar.txt")
                print("1 - Print start")
                print("2 - Print terminals")
                print("3 - Print nonterminals")
                print("4 - Print productions")
                print("0 - Back")
                opt2 = int(input("Choose: "))
                if opt2 == 1:
                    print(grammar.get_start())
                elif opt2 == 2:
                    print(grammar.get_terminals())
                elif opt2 == 3:
                    print(grammar.get_nonterminals())
                elif opt2 == 4:
                    print(grammar.get_productions())
        elif opt == 5:
            parser = Parser("grammar.txt")
            print(parser.get_first_set())
            print(parser.generate_follow_set())
            parser.create_table()