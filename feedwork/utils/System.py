from os import environ


def env(key, type_, default=None):
    """
    获取环境变量，可设置默认值。
    用法： flag = env("FLAG", bool, True)
    :param key: 环境变量名
    :param type_: 数据类型，支持： str , bool , int
    :param default: 默认值
    :return:
    """
    if key not in environ:
        return default

    val = environ[key]

    if type_ == str:
        return val
    elif type_ == bool:
        if val.lower() in ["1", "true", "yes", "y", "ok", "on"]:
            return True
        if val.lower() in ["0", "false", "no", "n", "nok", "off"]:
            return False
        raise ValueError(
            f"Invalid environment variable '{key}' ! expected boolean(true/false/yes/no/y/n/1/0) but '{val}'"
        )
    elif type_ == int:
        try:
            return int(val)
        except ValueError:
            raise ValueError(
                f"Invalid environment variable '{key}' ! expected an integer but '{val}'"
            ) from None
