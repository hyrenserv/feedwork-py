import os


def linecount(file):
    """
    得到文件的行数
    :param file: 文件全路经名或文件对象
    :return: 文件行数
    """

    def _linecount(fileObj) -> int:
        count = 0
        for _ in fileObj:
            count += 1
        return count

    # for count, line in enumerate(open(file_path)): pass
    if type(file) is str:
        with open(file, 'r') as f:
            return _linecount(f)
    else:
        return _linecount(file)


def size(filepath, readable=False):
    """
    得到文件大小
    :param filepath: 文件全路径
    :param readable: 是否返回带有计数单位的可读结果
    :return: 文件大小。数字，或带有KB/MB单位的文件大小
    """
    fstat = os.stat(filepath)
    fsize = fstat.st_size
    if readable:
        sizeMB = 1024 * 1024
        if fsize < sizeMB:
            return f"{fsize / 1024:.2f} KB"
        else:
            return f"{fsize / sizeMB:.2f} MB"
    else:
        return fstat.st_size


def write(file, content, append=False) -> None:
    """
    覆盖或追加写入文件
    :param file: 文件全路径或文件对象
    :param content: 写入的文本
    :param append: 是否为追加模式。如果file参数是文件对象，会忽略本参数
    :return: None
    """
    if type(file) is str:
        mode = 'w'
        if append:
            mode = 'a'
        with open(file, mode) as f:
            f.write(content)
    else:
        file.write(content)
