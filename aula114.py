def executes(function, *args):
    return function(*args)


#def sum(x, y):
    #return x + y


def create_multiplier(multiplier):
    def multiply(number):
        return number * multiplier
    return multiplier

#doubles = create_multiplier(2)
doubles = executes(
    lambda m: lambda n: n * m,
    2 
)
print(doubles(2))

print(
    executes(
        lambda x, y: x + y,
        2, 3
    )
)

print(
    executes(
        lambda *args: sum(args),
        1, 2, 3, 4, 5, 6
    )
)