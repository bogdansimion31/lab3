from model.languageSpecification import *


class ProgramInternalForm:
    def __init__(self):
        self.__content = []

    def add(self, code, id):
        self.__content.append((code, id))

    def __str__(self):
        return str(self.__content)

    def print_pif(self):
        for i in self.__content:
            print(f"{list(codification.keys())[list(codification.values()).index(i[0])]:<30}{'-'+'>'+' '+str(i[1]):<40}")

    def print_pif_to_file(self, my_file):
        f = open(my_file, "w")
        f.write("PIF: ")
        f.write("\n")
        for i in self.__content:
            f.write("\n")
            f.write(f"{list(codification.keys())[list(codification.values()).index(i[0])]:<30}{'-'+'>'+' '+str(i[1]):<40}")
        f.close()

