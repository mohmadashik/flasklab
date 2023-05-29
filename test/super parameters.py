class A(object):
    def __init__(self, foo, bar=3):
        self.foo = foo
        self.bar = bar

class B(A):
    def __init__(self, quux=6, **kwargs):
        super(B, self).__init__(**kwargs)

        self.quux = quux

# B(foo=1, quux=4)# AttributeError: 'A' object has no attribute 'quux'
c = B(quux=4,foo=1)
a = A(foo=5)
print(c.quux)
print(c.foo)

