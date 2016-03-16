# This segfaults under python-dbg
# (In a release build it "works" since the use-after-free happens without penalty.)

class C:
    def __getattr__(self, attr):
        del self
        print "C.__getattr__", attr
        del D.__get__
        raise AttributeError()

class D(object):
    __get__ = C()

class E(object):
    x = D()

try:
    print E().x
except Exception as e:
    print e
