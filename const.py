import sys


class Const:
    class ConstError(TypeError):
        pass

    def __setattr__(self, key, value):
        if self.__dict__.__contains__(key):
            raise self.ConstError("Can't rebind const(%s)" % key)
        self.__dict__[key] = value


sys.modules[__name__] = Const()
