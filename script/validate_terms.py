"""Validate that a specific Japanese word is always assigned to a certain English word

Usage:
  validate_terms.py <dict> <texfile>
  validate_terms.py (-h | --help)
Options:
  <dict>                tsv file which contains English key and Japanese values
  <texfile>             tex file to be checked
  -h --help             Show this screen.
"""

from utils import get_dict, LaTeXReader

from docopt import docopt
from logging import getLogger, StreamHandler, INFO

logger = getLogger(__name__)
handler = StreamHandler()
handler.setLevel(INFO)
logger.setLevel(INFO)
logger.addHandler(handler)


def validate(dic, iter_reader):
    code = 0

    for line_no, en, ja in iter_reader:
        en_lower = en.lower()
        for key, val in dic:
            if key in en_lower:
                if val not in ja:
                    error_msg = "[Term validation error] Found '{}' in L{} but Not found '{}' in L{}\n"\
                        .format(key, line_no, val, line_no + 1)
                    error_msg += "  L{}: {}\n".format(line_no, en.strip('\n'))
                    error_msg += "  L{}: {}".format(line_no + 1, ja.strip('\n'))
                    logger.error(error_msg)
                    code = 1
                else:
                    logger.info("[Successful term validation] L{}: {}, L{}, {}".format(line_no, key, line_no + 1, val))

    return code


def main():
    args = docopt(__doc__)
    dic_path = args['<dict>']
    tex_file = args['<texfile>']

    dic = get_dict(dic_path)
    reader = LaTeXReader(tex_file)

    code = validate(dic, reader)
    exit(code)


if __name__ == '__main__':
    main()
