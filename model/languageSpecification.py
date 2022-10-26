separators = ['[', ']', '{', '}', '(', ')', ';', ':', ',']
operators = ['+', '-', '*', '/', '%', '<', '<=', '=', '>=', '>',
             '>>', '<<', '==', '&', '|', '!=', '!']
reservedWords = ['char', 'int', 'bool', 'const', 'do', 'if', 'true', 'false',
                 'else', 'read', 'break', 'while', 'write', 'and', 'or', 'for']

everything = separators + operators + reservedWords
codification = dict([(everything[i], i + 2) for i in range(len(everything))])
codification['identifier'] = 0
codification['constant'] = 1