from logging import getLogger, StreamHandler, INFO

logger = getLogger(__name__)
handler = StreamHandler()
handler.setLevel(INFO)
logger.setLevel(INFO)
logger.addHandler(handler)


def load_tsv(path, num_col=2):
    """Load tsv file

    :type path: str
    :param path: path to tsv file
    :param num_col: int or list
    :rtype: list
    :return:

    Example:
    >>> l = load_terms("../resources/terms.tsv", [2, 3])
    >>> l = laod_list("../resources/modifier.txt", [1, 2])
    """

    def num_col_checker(num_col):
        if isinstance(num_col, int):
            return lambda line: len(line) == num_col

        if isinstance(num_col, list):
            return lambda line: num_col[0] <= len(line) <= num_col[1]

        raise AssertionError("num_col should list or int")

    checker = num_col_checker(num_col)

    try:
        with open(path, 'r') as f:
            lines = f.readlines()
    except:
        raise IOError("failed to load " + path)

    ret = [[x.strip('\n').strip() for x in line.split('\t')] for line in lines]
    for line in ret:
        if not checker(line):
            logger.info("Skip '{}'".format(line))

    return ret


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

                if line.startswith('%') and not line.startswith('% @suppress'):
                    ret.append(line_no)
                    ret.append(line)
                    flg = True

                line_no += 1
