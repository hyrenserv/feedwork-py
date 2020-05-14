import sys


class _Const(object):
    """
    用法：
    import feedwork.utils.Constant as const
    const.NAME = "fd"
    const.VALUE = 5
    """
    class ConstError(NameError): pass

    def __setattr__(self, name, value):
        if name in self.__dict__:  # 常量名已经存在，不能重新赋值
            raise self.ConstError(f"Constant name '{name}' already exists, you can't change value !")
        if not name.isupper():  # 所有的字母需要大写
            raise self.ConstError(f"Constant name '{name}' must be uppercase !")
        else:
            self.__dict__[name] = value

    # def __getattr__(self, name):
    #     if name in self.__dict__:
    #         return self.name
    #     else:
    #         return None


sys.modules[__name__] = _Const()
