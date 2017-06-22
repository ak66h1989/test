class Test:
    a=1
    def __init__(self, x):
        self.x = x+self.a
        self.a=2

    def foo1(self):
        print(self)
c=Test(2)
c.x
c.a
Test(2).a
c.foo1()

class test1(Test):
    pass

c=test1(2)
c.x
c.a
Test(2).a

class zzz():
    zoo = "zoo"

    @classmethod
    def foo(clss, name):
        print("hi! %s, it's classmethod." % name)
        print("zoo =", clss.zoo)

    @staticmethod
    def bar(name):
        print("hi! %s, it's staticmethod ." % name)
        print("zoo =", zzz.zoo)

    def normal_method(self):
        print("It's normal_method.")
        print("zoo =", self.zoo)

zzz.foo("mission")
print("="*20)
zzz.bar("mission")
print("="*20)
zzz().normal_method()
print("="*20)
zzz.normal_method(zzz)

class Kls(object):
    no_inst = 0

    def __init__(self):
        Kls.no_inst = Kls.no_inst + 1

    @classmethod
    def get_no_of_instance(cls_obj):
        return cls_obj.no_inst

ik1 = Kls()
ik2 = Kls()

print(ik1.get_no_of_instance())
print(Kls.get_no_of_instance())