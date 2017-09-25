def subcoro():
    # while True:
    #     x = yield
    #     print('x= ', x)
    # return "return subcoro"

    try:
        x = yield
        print('x1= ', x)
        x = yield
        print('x2= ', x)
    finally:
        print('finally')


def coro():
    while True:
        result = yield from subcoro()
        print('result= ', result)


gen = subcoro()

next(gen)
gen.send('test')
# gen.send('test2')
gen.close()
# gen.throw(StopIteration)



