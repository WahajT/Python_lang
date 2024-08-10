# We use * in function if we want to give more arguments which we do not want to write all



def Multi_Arguments(num,*numbers):
    print(type(numbers))

    Addition=num+sum(numbers)
    print(type(numbers))
    return Addition



print(Multi_Arguments(10,20,30))