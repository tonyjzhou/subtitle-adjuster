#!/usr/bin/env python3

from __future__ import print_function

import logging
import os
import os.path

from lib.files import is_valid_file_type, adjust_file
from lib.log_config import config_logger


def ask_user_input():
    srt_original = ask_valid_original_file_name()
    seconds = ask_valid_seconds()

    logging.debug("srt_original=%s", srt_original)
    logging.debug("seconds=%s", seconds)

    return srt_original, seconds


def ask_valid_seconds():
    while True:
        value = input('Enter seconds to add to or remove from original srt (e.g. 1 or -1): ')
        try:
            return int(value)
        except ValueError:
            print('\n\tInvalid integer value: "%s"\n\tPlease try again ...\n' % value)


def ask_valid_original_file_name():
    while True:
        file_name = input('Enter full file name for original srt (e.g. /Users/tonyzhou/Movies/abc.srt): ')

        if os.path.isfile(file_name) and is_valid_file_type(file_name):
            return file_name
        else:
            print('\n\tInvalid original file: "%s"\n\tPlease try again ...\n' % file_name)


def quit_gracefully():
    print('Bye')


def main():
    config_logger()

    try:
        adjust_file(*ask_user_input())
    except EOFError:
        quit_gracefully()


if __name__ == "__main__":
    main()
