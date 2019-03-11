import re
with open('test4.csv', 'r') as test:
    obj = []

    csv = test.read()

    test = csv.split('\n', 1)
    key, prop = test

    key = key.split(',')

    propList = []
    prop = prop.replace('\n', ' ').replace('\r', ' ')
    print(prop)

    while(len(prop) > 0):
        if prop[0] == '"':
            try:
                wordInQuote, rest = prop[1:].split('",', 1)
                wordInQuote = wordInQuote
                propList.append(wordInQuote)
                prop = rest
            except ValueError:
                wordInQuote = prop[1:-1]
                print(wordInQuote)
                propList.append(wordInQuote)
                prop = []

        else:
            try:
                nextWord, rest = prop.split(',', 1)
                propList.append(nextWord)
                prop = rest
            except ValueError:
                nextWord = prop
                propList.append(nextWord)
                prop = []

    resultObj = dict(zip(key, propList))
    # print(resultObj)
    # restText = "".join(b)
    # print(restText)

    # c, *d = b
    # print(a)
    # key = key.split(',')
    # resultObj = {}
    # result = c.split(',')

    # resultObj = dict(zip(key, result))
    # print(resultObj)
    # resultObj[x] = result[index]
    # print(resultObj)
    # b.split(',')
    # print(b)
