class ProgramInternalForm:
    def __init__(self):
        self.__pif = []

    def add(self, code, id):

        self.__pif.append((code, id))

    def __str__(self):
        return str(self.__pif)
