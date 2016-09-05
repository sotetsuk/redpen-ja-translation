"""Validate that a specific Japanese word is always assigned to a certain English word

Usage:
  validate_terms.py <terms> <texfile>
  validate_terms.py (-h | --help)
Options:
  <terms>               tsv file which contains English key and Japanese values and (if exists) Exception
  <texfile>             tex file to be checked
  -h --help             Show this screen.
"""

from utils import load_terms, LaTeXReader

from docopt import docopt
from logging import getLogger, StreamHandler, INFO

logger = getLogger(__name__)
handler = StreamHandler()
handler.setLevel(INFO)
logger.setLevel(INFO)
logger.addHandler(handler)


def validate_terms(terms, iter_reader):
    code = 0

    for line_no, en, ja in iter_reader:
        en_lower = en.lower()
        for term in terms:
            has_exception = False
            if len(term) == 2:
                key, val = term
            if len(term) == 3:
                key, val, exception_list = term
                exception_list = [exception.lower() for exception in exception_list]
                has_exception = True
            if key in en_lower:
                if val not in ja:
                    if has_exception:
                        for exception in exception_list:
                            if exception in en_lower:
                                info_msg = "[Skipped term validation] Found '{}' in L{} and found '{}' in L{}".format(key, line_no, exception, line_no)
                                logger.info(info_msg)
                                break
                    else:
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

    terms = load_terms(terms_path)
    reader = LaTeXReader(tex_file)

    code = validate_terms(terms, reader)
    exit(code)


if __name__ == '__main__':
    main()
