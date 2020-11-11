from FiniteAutomata import *

if __name__ == '__main__':
    fa = FiniteAutomata()
    fa.readFile("fa.txt")
    opt=100
    while opt!=0:
        print("1-Print states,alphabet,transitions and final states")
        print("2-Verify if FA is deterministic")
        print("3-Enter sequence and see if accepted")
        opt=int(input("Pick one"))
        if opt==1:
            fa.printAll()
        elif opt==2:
            print(fa.checkIfDeterministic())
        elif opt==3:
            seq=str(input("enter sequence: "))
            print(fa.isAccepted(seq))