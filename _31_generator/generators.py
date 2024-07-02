def generator(num):
    while num > 0:
        yield num
        num -= 1


values = generator(5)
print(next(values))
print(type(next(values)))
print(next(values))


def list_generator(list):
    for i in list:
        yield i
list=[1,2,3,4,5]
values  = list_generator(list)
print(next(values))
print(next(values))
print(next(values))
list.append(11)
print(next(values))
print(next(values))
print(next(values))
