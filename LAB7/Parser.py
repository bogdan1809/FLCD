from Grammar import Grammar


class Parser:
    def __init__(self, fileName):
        self.__grammar = Grammar(fileName)
        self.__firstSet = {}
        self.__followSet = {}
        self.generate_first_set()
        self.__parsing_table = {}

    def generate_first_set(self):

        for nonterminal in self.__grammar.get_nonterminals():
            first = self.first_of_nonterminal(nonterminal)
            self.__firstSet[nonterminal] = first

    def first_of_nonterminal(self, nonterminal):
        firstSet = []
        if nonterminal in self.__firstSet.keys():
            return self.__firstSet[nonterminal]
        productions = self.__grammar.get_productions()
        for rule in productions[nonterminal]:
            i = 0
            firstSymbol = rule[i]
            while i < len(rule) - 1:
                if firstSymbol == "epsilon":
                    i = i + 1
                    firstSymbol = rule[i]
                else:
                    break

            if i == len(rule) - 1 and firstSymbol == "epsilon":
                firstSet.append("epsilon")

            elif firstSymbol in self.__grammar.get_terminals():

                firstSet.append(firstSymbol)
            else:
                firstSet.extend(self.first_of_nonterminal(firstSymbol))
        return firstSet

    def get_first_set(self):
        return self.__firstSet

    def generate_follow_set(self):
        for nonterminal in self.__grammar.get_nonterminals():
            follow = self.follow_of(nonterminal)
            self.__followSet[nonterminal] = follow
        print(self.__followSet)

    def follow_of(self, nonterminal):
        followSet = []
        productions = self.__grammar.get_productions()
        if nonterminal in self.__followSet.keys():
            return self.__followSet[nonterminal]

        if nonterminal == self.__grammar.get_start():
            followSet.append("$")

        for production in productions.items():

            for elem in production[1]:
                for i in range(len(elem)):
                    if elem[i] == nonterminal:
                        if i < len(elem) - 1:

                            if elem[i + 1] in self.__grammar.get_terminals():
                                followSet.append(elem[i + 1])
                            if elem[i + 1] in self.__grammar.get_nonterminals():
                                followSet.extend(self.__firstSet[elem[i + 1]])
                        else:
                            followSet.extend(self.follow_of(production[0]))
        return followSet

    def get_follow_set(self):
        return self.__followSet

    def create_table(self):
        nonterminals = self.__grammar.get_nonterminals()
        terminals = self.__grammar.get_terminals()
        terminals.append("$")
        for nonterminal in nonterminals:
            for terminal in terminals:
                self.__parsing_table[(nonterminal, terminal)] = 0

        productions = self.__grammar.get_productions()

        productionIndex = 1
        for entry in productions.items():
            for production in entry[1]:
                for item in production:
                    if item in terminals:
                        self.__parsing_table[(entry[0], item)] = productionIndex
                    elif item == "epsilon":
                        follow = self.__followSet[entry[0]]
                        for elem in follow:
                            self.__parsing_table[(entry[0], elem)] = productionIndex
                    elif item in nonterminals:
                        first = self.__firstSet[item]
                        for elem in first:
                            self.__parsing_table[(entry[0], elem)] = productionIndex
                productionIndex += 1

        for cell in self.__parsing_table.items():
            print(cell)
