def mydef(cls):
    def creation():
        print(cls.__qualname__)
    creation()
    return cls
class MyMetaclass(type):
    def __new__(cls, name, bases, clsdict):
        clsobj = super().__new__(cls, name, bases, clsdict)
        clsobj = mydef(clsobj)
        return clsobj

class A(metaclass=MyMetaclass):
    pass