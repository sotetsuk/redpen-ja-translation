"""Validate that the same modifier is also used in translated sentence.

Usage:
  validate_modifier.py <list> <texfile>
  validate_modifier.py (-h | --help)
Options:
  <list>                list of modifier (e.g., \em, \bf)
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


def validate_modifier(l, iter_reader):
    code = 0

    for line_no, en, ja in iter_reader:
        en_lower = en.lower()
        for mods in l:
            has_exception = False

            if len(mods) == 1:
                mod = mods[0]
            if len(mods) == 2:
                mod, exception_list = mods
                exception_list = [exception.strip().lower() for exception in exception_list.split(',')]
                has_exception = True

            if mod in en_lower:
                if mod not in ja:
                    if has_exception:
                        for exception in exception_list:
                            if exception in en_lower:
                                info_msg = "[Skipped modifier validation] Found '{}' in L{} and found '{}' in L{}".format(mod, line_no, exception, line_no)
                                logger.info(info_msg)
                                break
                    else:
                        error_msg = "[Modifier validation error] Found '{}' in L{} but Not found '{}' in L{}\n" \
                            .format(mod, line_no, mod, line_no + 1)
                        error_msg += "  L{}: {}\n".format(line_no, en.strip('\n'))
                        error_msg += "  L{}: {}".format(line_no + 1, ja.strip('\n'))
                        logger.error(error_msg)
                        code = 1
                else:
                    logger.info("[Successful Modifier validation] L{}: {}, L{}, {}".format(line_no, mod, line_no + 1, mod))

    return code


def main():
    args = docopt(__doc__)
    list_path = args['<list>']
    tex_file = args['<texfile>']

    l = load_tsv(list_path, [1, 2])
    reader = LaTeXReader(tex_file)

    code = validate_modifier(l, reader)
    exit(code)


if __name__ == '__main__':
    main()
