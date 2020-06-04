from os import environ


def env(key, var_type=str):
    if key not in environ:
        raise ValueError(
            f"Environment variable '{key}' not exist !"
        )
    return envOrDefault(key, var_type)


def envOrDefault(key, var_type, default=None):
    """
    获取环境变量，可设置默认值。
    用法： flag = env("FLAG", bool, True)
    :param key: 环境变量名
    :param var_type: 数据类型，支持： str , bool , int
    :param default: 默认值
    :return:
    """
    if key not in environ:
        return default

    val = environ[key]

    if var_type == str:
        return val
    elif var_type == bool:
        if val.lower() in ["1", "true", "yes", "y", "ok", "on"]:
            return True
        if val.lower() in ["0", "false", "no", "n", "nok", "off"]:
            return False
        raise ValueError(
            f"Invalid environment variable '{key}' ! expected boolean(true/false/yes/no/y/n/1/0) but '{val}'"
        )
    elif var_type == int:
        try:
            return int(val)
        except ValueError:
            raise ValueError(
                f"Invalid environment variable '{key}' ! expected an integer but '{val}'"
            ) from None
    else:
        raise ValueError(
            f"Unsupported variable type({var_type}) by '{key}' !"
        ) from None