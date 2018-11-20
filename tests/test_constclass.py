import pytest

from constclass import constclass, constmethod, ConstWarning, ConstError


def test_constmethod():

    @constclass
    class Thing:
        def __init__(self, a, b):
            self.a = a
            self.b = b

        def modify(self):
            self.b, self.a = self.a, self.b

        @constmethod
        def const(self):
            self.b = 10
            return self.a, self.b

    instance = Thing(5, 6)

    with pytest.raises(ConstError):
        instance.const()

    assert instance.b == 6
    # This should not raise an error
    instance.b = 10
    assert instance.b == 10


def test_constmethod_warning():

    @constclass(warning=True)
    class Thing:
        def __init__(self, a, b):
            self.a = a
            self.b = b

        def modify(self):
            self.b, self.a = self.a, self.b

        @constmethod
        def const(self):
            self.b = 10
            return self.a, self.b

    instance = Thing(5, 6)

    with pytest.warns(ConstWarning):
        instance.const()


def test_constmethod_complex():

    @constclass
    class Thing:
        def __init__(self, a, b):
            self.a = a
            self.b = dict(b=b)

        def modify(self):
            self.b, self.a = self.a, self.b

        @constmethod
        def const(self):
            self.b['b'] = 10
            return self.a, self.b

    instance = Thing(5, 6)

    with pytest.raises(ConstError):
        instance.const()
