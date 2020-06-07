import os
import yaml

from feedwork.utils import logger
import feedwork.utils.System as sysu 


HRS_RESOURCES_ROOT = sysu.env("HRS_RESOURCES_ROOT", str)  # 所有资源根目录
if not os.path.isdir(HRS_RESOURCES_ROOT):
    raise RuntimeError(f"env [HRS_RESOURCES_ROOT={HRS_RESOURCES_ROOT}] is not regular dir !")
_HRS_FDCONFIG_ROOT = os.path.join(HRS_RESOURCES_ROOT, "fdconfig")
logger.debug(f"[load_conf] _HRS_FDCONFIG_ROOT={_HRS_FDCONFIG_ROOT}")


class AutowaredBeanByDict(dict):
    __setattr__ = dict.__setitem__
    __getattr__ = dict.__getitem__


def dictToBean(dictObj):
#     print(type(dictObj), dictObj)
    if not isinstance(dictObj, dict):
        return dictObj
    inst = AutowaredBeanByDict()
    for k, v in dictObj.items():
        inst[k] = dictToBean(v)
    return inst

def load_conf(filename :str, *, return_type="bean"):
    conf_file = os.path.join(_HRS_FDCONFIG_ROOT, filename)
    if not os.path.isfile(conf_file):
        raise RuntimeError(f"config file [{conf_file}] is not regular file !")
    with open(conf_file, "r") as f:
        data = yaml.safe_load(f)
#         print(conf_file, type(data), data)
    if return_type == "bean":
        return dictToBean(data)
    elif return_type == "dict":
        return data
    else:
        raise ValueError(f"Invalid return_type ! expected 'bean, dict' but '{return_type}'")


if __name__ == "__main__":
    # TODO 删掉 main！ 写到test_suite中去
    dbinfo1 = load_conf("dbinfo.conf", return_type="bean")
    assert type(dbinfo1) == AutowaredBeanByDict
    dbinfo2 = load_conf("dbinfo.conf", return_type="dict")
    assert type(dbinfo2) == dict
    
    assert dbinfo1['global'].fetch_size == dbinfo2['global']['fetch_size']
    print(type(dbinfo1))
    print(dbinfo1['global'].fetch_size)
