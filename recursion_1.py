def hello(x):
    if x == 0:
        return
    else:
        print('Hello World')
        hello(x - 1)

hello(3)