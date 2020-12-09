class Grammar:
    def __init__(self, fileName):
        self.__terminals = []
        self.__nonterminals = []
        self.__productions = {}
        self.__s = ""
        self.read_grammar_from_file(fileName)

    def check_start_symbol(self):
        if self.__s not in self.__nonterminals:
            raise Exception(f"Starting symbol {self.__s} not in nonterminals list")

    def check_production(self):
        for nonterminal in self.__productions.keys():
            if nonterminal not in self.__nonterminals:
                raise Exception(f"{nonterminal} not in the list of nonterminals.")

            for symbols in self.__productions[nonterminal]:
                for symbol in symbols:
                    if symbol not in self.__terminals and symbol not in self.__nonterminals and symbol !="epsilon":
                        raise Exception(f"{symbol} not in any list")

    def read_grammar_from_file(self, fileName):
        with open(fileName, "r") as file:
            self.__nonterminals = file.readline().strip().split(" ")
            self.__terminals = file.readline().strip().split(" ")
            self.__s = file.readline().strip()
            for line in file.readlines():
                self.__productions[line.split("-")[0].strip()] = [val.strip().split(" ") for val in
                                                                  line.split("-")[1].strip().split("|")]

            self.check_start_symbol()
            self.check_production()

    def get_terminals(self):
        return self.__terminals

    def get_nonterminals(self):
        return self.__nonterminals

    def get_productions(self):
        return self.__productions

    def get_start(self):
        return self.__s
