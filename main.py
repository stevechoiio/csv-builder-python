import re
with open('test3.csv', 'r') as test:
    obj = []

    csv = test.read()

    key, info = csv.split('\n', 1)
    key = key.split(',')
    # print(info)
    parsedInfo = re.findall(
        '[a-zA-Z0-9\s:]+|"[\s0-9a-zA-Z,]+"', info)

    print(len(key))

    for word in parsedInfo:
        parsedInfo.extend(word.split('\r\n'))

    print(len(parsedInfo))
    print(parsedInfo)
