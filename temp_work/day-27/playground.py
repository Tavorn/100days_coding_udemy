def add(*args):
    print(args[1])
    sum_num = 0
    for num in args:
        print(num)
        sum_num += num
    return sum_num


# print(add(3, 5, 9, 1, 4, 5, 2, 5))


def calculate(n, **kwargs):
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    #
    # print(kwargs["add"])
    # print(kwargs["multiply"])
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)


class Car:

    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")
        # self.make = kwargs["make"]
        # self.model = kwargs["model"]
        self.colour = kwargs.get("colour")
        self.seats = kwargs.get("seats")


# my_car = Car(make="Nissan", model="GT-R")
my_car = Car(make="Nissan", model="GT-R")
print(my_car.model)


