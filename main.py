with open('test3.csv', 'r') as test3:
    obj = []

    test = test3.read()

    test = test.splitlines()
    a, *b = test
    c, *d = b
    # print(a)
    key = a.split(',')
    resultObj = {}
    result = c.split(',')

    resultObj = dict(zip(key, result))
    print(resultObj)
    # resultObj[x] = result[index]
    # print(resultObj)
    # b.split(',')
    # print(b)
