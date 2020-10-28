import re
import tokenList


def getStringToken(line, index):
    token = ''
    quote = 0

    while index < len(line) and quote < 2:
        if line[index] == '"':
            quote += 1
        token += line[index]
        index += 1

    return token, index


def isPartOfOperator(char):
    for op in tokenList.operators:
        if char in op:
            return True
    return False


def getOperatorToken(line, index):
    token = ''

    while index < len(line) and isPartOfOperator(line[index]):
        token += line[index]
        index += 1

    return token, index


def get_tokens(line, separators):
    token = ''

    index = 0
    tokenList = []
    line = line.strip()

    while index < len(line):
        if line[index] == '"':
            if token:

                tokenList.append(token)

            token, index = getStringToken(line, index)

            tokenList.append(token)
            token = ''

        elif isPartOfOperator(line[index]):
            if token:
                tokenList.append(token)

            token, index = getOperatorToken(line, index)

            tokenList.append(token)
            token = ''
        elif line[index] in separators:
            if token:
                tokenList.append(token)

            token, index = line[index], index + 1

            tokenList.append(token)
            token = ''
        else:
            token += line[index]
            index += 1

    if token:
        tokenList.append(token)
    return tokenList


def isIdentifier(token):
    return re.match(r'^[a-zA-Z]([a-zA-Z]|[0-9]){,255}$', token) is not None


def isConstant(token):
    return re.match('^(0|[\+\-]?[1-9][0-9]*)$|^\".*\"$', token) is not None
