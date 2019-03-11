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

    newInfo = []
    for i in parsedInfo:
        newInfo += (i.split('\r\n'))

    print(len(newInfo))
    # print(parsedInfo)
