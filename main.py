from model.symbolTable import *
from model.programInternalForm import *
from model.scanner import *
from model.languageSpecification import codification

def main():
    # pif = ProgramInternalForm()
    # st = SymbolTable()
    # run("p1.txt",pif,st)
    # print('Program Internal Form: \n')
    # pif.print_pif()
    # print('\nSymbol Table: \n')
    # x=codification
    # print(x)
    # print('\n')
    # st.print_st()
    file_name = 'p2.txt'

    st = SymbolTable()
    pif = ProgramInternalForm()

    # with open(file_name, 'r') as file:
    #     for line in file:
    #         print([token for token in token_generator(line)])

    with open(file_name, 'r') as file:
        lineNo = 0
        for line in file:
            lineNo += 1
            for token in token_generator(line[0:-1]):
                if token in separators + operators + reservedWords and token != ' ':
                    pif.add(codification[token], -1)
                elif is_identifier(token):
                    id = st.add(token)
                    pif.add(codification['identifier'], id)
                elif is_constant(token):
                    id = st.add(token)
                    pif.add(codification['constant'], id)
                else:
                    if token!=' ':
                        raise Exception('LEXICAL ERROR : '+'Unknown token ' + token + ' at line ' + str(lineNo))

    print("lexically correct!")


if __name__ == '__main__':
    main()
