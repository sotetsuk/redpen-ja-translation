"""Validate that a specific Japanese word is always assigned to a certain English word

Usage:
  validate_terms.py <terms> <texfile>
  validate_terms.py (-h | --help)
Options:
  <terms>               tsv file which contains English key and Japanese values and (if exists) Exception
  <texfile>             tex file to be checked
  -h --help             Show this screen.
"""

from utils import load_tsv, LaTeXReader

from docopt import docopt
from logging import getLogger, StreamHandler, INFO

logger = getLogger(__name__)
handler = StreamHandler()
handler.setLevel(INFO)
logger.setLevel(INFO)
logger.addHandler(handler)


def validate_terms(terms, iter_reader):

    def _exists(l, str):
        for e in l:
            if e in str:
                return True
        return False

    def _found(l, str):
        for e in l:
            if e in str:
                return e
        return None

    code = 0

    for line_no, en, ja in iter_reader:
        en_lower = en.lower()
        for term in terms:
            has_exception = False
            if len(term) == 2:
                key, val = term
            if len(term) == 3:
                key, val, exception_list = term
                exception_list = [exception.strip().lower() for exception in exception_list.split(',')]
                has_exception = True
            if not val:
                continue
            if key in en_lower:
                if val not in ja:
                    if has_exception and _exists(exception_list, en_lower):
                        info_msg = "[Skipped term validation] Found '{}' in L{} and found '{}' in L{}".format(key, line_no, _found(exception_list, en_lower), line_no)
                        logger.info(info_msg)
                        break
                    error_msg = "[Term validation error] Found '{}' in L{} but Not found '{}' in L{}\n" \
                        .format(key, line_no, val, line_no + 1)
                    error_msg += "  L{}: {}\n".format(line_no, en.strip('\n'))
                    error_msg += "  L{}: {}".format(line_no + 1, ja.strip('\n'))
                    logger.error(error_msg)
                    code = 1
                else:
                    info_msg = "[Successful term validation] Found '{}' in L{} and found '{}' in L{}" \
                        .format(key, line_no, val, line_no + 1)
                    logger.info(info_msg)

    return code


def main():
    args = docopt(__doc__)
    terms_path = args['<terms>']
    tex_file = args['<texfile>']

    terms = load_tsv(terms_path, [2, 3])
    reader = LaTeXReader(tex_file)

    code = validate_terms(terms, reader)
    exit(code)


if __name__ == '__main__':
    main()
