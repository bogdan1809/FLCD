class FiniteAutomata:
    def readLine(self, line):
        line = line.strip().split('=')

        line = line[1].strip().split(',')

        return [value.strip('{').strip('}').strip() for value in line]

    def readFile(self, fileName):
        with open(fileName) as file:
            Q = self.readLine(file.readline())
            E = self.readLine(file.readline())
            q0 = file.readline().split('=')[1].strip()

            F = self.readLine(file.readline())

            S = []

            for line in file:
                self.readTransition(line, S)
            print(Q, '\n', E, '\n', q0, '\n', F)
            print(S)
            print(self.isDeterministic(S))


    def readTransition(self, line, result):

        if len(line.split('->')) > 1:
            lhs, rhs = line.split('->')
            newState = rhs.strip()
            oldState, route = [value.strip() for value in lhs.split(',')]

            result.append(((oldState.strip('('), route.strip(')')), newState.strip(',')))


    def isDeterministic(self, transitions):
        lista = []
        for transition in transitions:
            lista.append(transition[1])
        if len(set(lista)) == len(lista):
            return True
        return False
