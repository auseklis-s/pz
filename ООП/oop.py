class Car():
    @staticmethod
    def move():
        print('машина едет')

    def stop():
        print('машина стоит')

my_car = Car()
my_car1 = Car()

# my_car.move()
# my_car.stop()
# my_car.move()
# my_car.move()
# my_car1.stop()

# print(my_car)
# print(type(my_car))
# print(isinstance(my_car, Car))
# print(isinstance(my_car, object))
# print(my_car == my_car1)
# print(id(my_car), id(my_car1))


# print(dir(my_car))
print(my_car.__dict__)