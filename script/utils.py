def load_list(path):
    """Load list file.

    :type path: str
    :param path: path to txt file
    :rtype: dict
    :return:

    Example:
    >>> l = laod_list("../resources/modifier.txt")
    """

    try:
        with open(path, 'r') as f:
            lines = f.readlines()
    except:
        raise IOError("failed to load " + path)

    l = [line.strip().strip('\n') for line in lines]

    return l


def load_terms(path):
    """Load tsv dictionary file.

    :type path: str
    :param path: path to tsv file
    :rtype: dict
    :return:

    Example:
    >>> dic = load_terms("../resources/terms.tsv")
    """

    try:
        with open(path, 'r') as f:
            lines = f.readlines()
    except:
        raise IOError("failed to load " + path)

    dic = [[x.strip('\n').strip() for x in line.split('\t')] for line in lines]
    for line in dic:
        if len(line) > 3 or len(line) < 2:
            raise IOError("failed to parse " + path)

    return dic


class LaTeXReader(object):
    """Read LaTeX files

    Example:
    >>> reader = LaTeXReader("../tex/main.tex")
    >>> for line in reader:
    ...     print(line)
    """

    def __init__(self, path):
        self.path = path

    def __iter__(self):

        with open(self.path, 'r') as f:
            line_no = 1
            ret = []
            flg = False
            for line in f:
                if flg:
                    ret.append(line)
                    flg = False
                    yield ret
                    ret = []

                if line.startswith('%'):
                    ret.append(line_no)
                    ret.append(line)
                    flg = True

                line_no += 1