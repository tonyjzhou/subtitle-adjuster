from __future__ import print_function

import logging

from line_adjuster import adjust
from log_config import config_logger


def adjust_file(srt_original, srt_new, seconds):
    with open(srt_original, "r", encoding='utf-8') as orig_file:
        with open(srt_new, "w", encoding='utf-8') as new_file:
            for line in orig_file.readlines():
                print(adjust(line, seconds), file=new_file)
    logging.info("Generated new srt as %s", srt_new)


def user_input():
    srt_original = input('Enter full srt original file path: ')
    srt_new = input('Enter full srt new file path: ')
    seconds = input('Enter seconds to add to or remove from (negative number) original srt: ')

    logging.debug("srt_original=%s", srt_original)
    logging.debug("srt_new=%s", srt_new)
    logging.debug("seconds=%s", seconds)

    return srt_original, srt_new, seconds


def main():
    config_logger()
    adjust_file(*user_input())


if __name__ == "__main__":
    main()
