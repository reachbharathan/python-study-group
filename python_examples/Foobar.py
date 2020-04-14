class FooBar(object):
    __slots__ = ["foo", "bar", "baz","temp"]
    # if you don't define __slots__, you can add attr to the object as needed
    # if you do, the object can only contain those attributes.

    def __init__(self, foo=None, bar=None, baz=None):
        self.foo = foo
        self.bar = bar
        self.baz = baz

    def __str__(self):
        return "I'm a FooBar with id {0} with foo: {1.foo}, bar: {1.bar}, baz: {1.baz}".format(id(self), self)

a = FooBar("a","B","CCC")

a.temp = "New Assignment"
print(a.__str__())
print(a.__slots__)
a.dummy = "dummy"
