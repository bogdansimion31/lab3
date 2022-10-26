import re

from model.languageSpecification import *
from model.symbolTable import *
from model.programInternalForm import *


def run(file_name, pif, st):
    file = open(file_name)
    data = file.read()
    program = data.split("\n")
    line_no = 0
    for line in program:
        line_no = line_no + 1
        print([token for token in token_generator(line)])
        for token in token_generator(line):
            if token in separators + operators + reservedWords and token != ' ':
                pif.add(codification[token], -1)
            elif is_identifier(token):
                id = st.add(token)
                pif.add(codification['identifier'], id)
            elif is_constant(token):
                id = st.add(token)
                pif.add(codification['constant'], id)
            else:
                if token != ' ':
                    raise Exception('Unknown token ' + token + ' at line ' + str(line_no))


def token_generator(line):
    token = ''
    index = 0
    while index < len(line):
        if line[index] == '"':
            if token:
                yield token
            token, index = get_string_token(line, index)
            index= index+1
            yield token
            token = ''
        elif is_part_of_operator(line[index]):
            if token:
                yield token
            token, index = get_operator_token(line, index)
            yield token
            token = ''
        elif line[index] in separators:
            if token:
                yield token
            token = line[index]
            index = index + 1
            yield token
            token = ''
        elif line[index] == ' ':
            if token:
                yield token
            token = ''
            index = index + 1
        else:
            token += line[index]
            index += 1
    if token:
        yield token


def is_part_of_operator(char):
    for op in operators:
        if char in op:
            return True
    return False


def get_operator_token(line, index):
    token = ''
    while index < len(line) and is_part_of_operator(line[index]):
        token += line[index]
        index += 1

    return token, index


def get_string_token(line, index):
    token = ''
    quote_count = 0

    while index < len(line) and quote_count < 2:
        if line[index] == '"':
            quote_count += 1
        else:
            token += line[index]
        index += 1
    return token, index


def is_identifier(token):
    return re.match(r'^[a-zA-Z]([a-zA-Z]|[0-9]){,7}$', token) is not None


def is_constant(token):
    return re.match('^(0|[\+\-]?[1-9][0-9]*)$|^\'.\'$|^\".*\"$', token) is not None
# import re
#
# from model.languageSpecification import *
#
#
# def is_part_of_operator(char):
#     for op in operators:
#         if char in op:
#             return True
#     return False
#
#
# def is_escaped_quote(line, index):
#     return False if index == 0 else line[index - 1] == '\\'
#
#
# def get_string_token(line, index):
#     token = ''
#     quoteCount = 0
#
#     while index < len(line) and quoteCount < 2:
#         if line[index] == '"' and not is_escaped_quote(line, index):
#             quoteCount += 1
#         token += line[index]
#         index += 1
#
#     return token, index
#
#
# def get_operator_token(line, index):
#     token = ''
#     while index < len(line) and is_part_of_operator(line[index]):
#         token += line[index]
#         index += 1
#
#     return token, index
#
#
# def token_generator(line, separators):
#     token = ''
#     index = 0
#
#     while index < len(line):
#         if line[index] == '"':
#             if token:
#                 yield token
#             token, index = get_string_token(line, index)
#             yield token
#             token = ''
#
#         elif is_part_of_operator(line[index]):
#             if token:
#                 yield token
#             token, index = get_operator_token(line, index)
#             yield token
#             token = ''
#
#         elif line[index] in separators:
#             if token:
#                 yield token
#             token, index = line[index], index + 1
#             yield token
#             token = ''
#
#         else:
#             token += line[index]
#             index += 1
#     if token:
#         yield token
#
#
# def is_identifier(token):
#     return re.match(r'^[a-zA-Z]([a-zA-Z]|[0-9]|_){,7}$', token) is not None
#
#
# def is_constant(token):
#     return re.match('^(0|[\+\-]?[1-9][0-9]*)$|^\'.\'$|^\".*\"$', token) is not None
