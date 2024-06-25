# Method overloading using default argument and variable length arguments
class Polymorphism:

    def start_engine(self, a=None, b=None):
        if a is not None and b is not None:
            print(a, b)
        elif a is not None:
            print(a)
        else:
            print(b)

    def start_drive(self, *args, **kwargs):
        if args:
            print(args)
        if kwargs:
            print(kwargs)


ob = Polymorphism()
ob.start_engine(6)  # print 6
ob.start_engine(8, 5)  # print 8 5
ob.start_drive(1, 3, 7, 9)
ob.start_drive(mass=5, buble=10)


# method overriding
class Enemy:
    def loud(self):
        print("speakers")


class Friend:
    def loud(self):
        print("earphones")


class Neighbour(Enemy, Friend):
    def loud(self):
        print("Soundbars")


obt = Neighbour()
obt.loud()
