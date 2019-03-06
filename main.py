with open('test3.csv','r') as test3:
    test = test3.read()
    (test,...a) = test.splitlines()
    print(test)
    print(a)

