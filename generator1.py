def square(i):
    #0,1,2,3,4,5,6,7,8,9
    for i in range(i):
        if i>5:
            print(i)
            yield i
square(10)
for i in square(10):
    print(i)