import inspect


CONST_ATTR = '__check_const__'


class ConstError(Exception):
    pass


def check_const(self, attr, value):
    raise ConstError('Attempted to set {} in method marked const', str(attr))


def constmethod(method):
    def method_check_const(self, *args, **kwargs):
        try:
            setattr(self, CONST_ATTR, True)
            return method(self, *args, **kwargs)
        finally:
            setattr(self, CONST_ATTR, False)

    return method_check_const


def constclass(cls):

    orig_setattr = cls.__setattr__

    def const_check(self, attr, value):
        if attr != CONST_ATTR and getattr(self, CONST_ATTR, False):
            msg = "Set attribute '{}' in a method marked const"
            raise ConstError(msg.format(attr))

        return orig_setattr(self, attr, value)

    cls.__setattr__ = const_check
    return cls
