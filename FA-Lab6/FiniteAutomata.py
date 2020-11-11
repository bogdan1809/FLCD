class FiniteAutomata:
    def __init__(self):
        self.Q = None
        self.E = None
        self.q0 = None
        self.F = None
        self.S = None

    def readLine(self, line):
        line = line.strip().split('=')

        line = line[1].strip().split(',')

        return [value.strip('{').strip('}').strip() for value in line]

    def readFile(self, fileName):
        with open(fileName) as file:
            self.Q = self.readLine(file.readline())
            self.E = self.readLine(file.readline())
            self.q0 = file.readline().split('=')[1].strip()

            self.F = self.readLine(file.readline())

            self.S = []

            for line in file:
                self.readTransition(line, self.S)

    def printAll(self):
        print(self.Q, '\n', self.E, '\n', self.q0, '\n', self.F)
        print(self.S)

    def checkIfDeterministic(self):
        return self.isDeterministic(self.S)

    def readTransition(self, line, result):

        if len(line.split('->')) > 1:
            lhs, rhs = line.split('->')
            newState = rhs.strip()
            oldState, route = [value.strip() for value in lhs.split(',')]
            trans = ((oldState.strip('('), route.strip(')')), newState.strip(', '))
            if trans not in result:
                result.append(trans)
            #result.append(((oldState.strip('('), route.strip(')')), newState.strip(',')))

    def isDeterministic(self, transitions):
        lista = []
        transitionset = set()
        for transition in transitions:
            lista.append(transition[1])
            transitionset.add(transition[0])
        if len(set(transitionset)) == len(lista):
            return True
        return False

    def isAccepted(self, sequence):
        if self.isDeterministic(self.S):
            state = self.q0

            while (len(sequence) > 0):
                elem = sequence[0]
                key = (state, elem)
                ok = 0
                for transition in self.S:
                    if key == transition[0]:
                        state = transition[1]
                        sequence = sequence[1:]
                        ok = 1
                if ok == 0:
                    return False
            if state in self.F:
                return True
            return False
