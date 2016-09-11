from __future__ import print_function

import logging
import os

from line_adjuster import adjust
from log_config import config_logger


def make_new_filename(filename):
    base, extension = os.path.splitext(filename)
    logging.debug("base=%s" % base)
    logging.debug("extension=%s" % extension)
    return '{0}_new{1}'.format(base, extension)


def adjust_file(filename, seconds):
    new_filename = make_new_filename(filename)

    with open(filename, "r") as srt_file:
        with open(new_filename, "w") as new_file:
            for line in srt_file.readlines():
                print(adjust(line, seconds), file=new_file)
    logging.info("Generated new srt as %s", new_filename)


def main():
    config_logger()
    adjust_file("srt/Captain.America.Civil.War.2016.1080p.BluRay.x264-[YTS.AG].srt", 22)


if __name__ == "__main__":
    main()
