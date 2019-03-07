
with open('test4.csv', 'r') as test:
    obj = []

    csv = test.read()

    test = csv.split('\n', 1)
    key, prop = test

    propList = []

    while(len(prop) > 0):
        if prop[0] == '"':
            try:
                wordInQuote, rest = prop[1:].split('",', 1)
                wordInQuote = wordInQuote.replace('\n', '')
                propList.append(wordInQuote)
                prop = rest
            except ValueError:
                wordInQuote = prop[1:-1].replace('\n', '')
                print(wordInQuote)
                propList.append(wordInQuote)
                prop = []

        else:
            nextWord, rest = prop.split(',', 1)

            propList.append(nextWord)

            prop = rest
        print(propList)

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
