#!/usr/bin/env python3

from __future__ import print_function

import logging
import os
import os.path

from lib.log_config import config_logger
from lib.files import make_new_base_name, is_valid_file_type, adjust_file


def ask_user_input():
    srt_original = ask_valid_original_file_name()
    srt_new_path = ask_valid_new_path_name()
    seconds = ask_valid_seconds()

    logging.debug("srt_original=%s", srt_original)
    logging.debug("srt_new_path=%s", srt_new_path)
    logging.debug("seconds=%s", seconds)

    return srt_original, srt_new_path, seconds


def ask_valid_seconds():
    while True:
        value = input('Enter seconds to add to or remove from original srt (e.g. 1 or -1): ')
        try:
            return int(value)
        except ValueError:
            print('\n\tInvalid integer value: "%s"\n\tPlease try again ...\n' % value)


def ask_valid_new_path_name():
    while True:
        path_name = input('Enter path for the new srt (e.g. /Users/tonyzhou/Movies): ')

        if os.path.isdir(path_name):
            return path_name
        else:
            print('\n\tInvalid new path: "%s"\n\tPlease try again ...\n' % path_name)


def ask_valid_original_file_name():
    while True:
        file_name = input('Enter full file name for original srt (e.g. /Users/tonyzhou/Movies/abc.srt): ')

        if os.path.isfile(file_name) and is_valid_file_type(file_name):
            return file_name
        else:
            print('\n\tInvalid original file: "%s"\n\tPlease try again ...\n' % file_name)


def main():
    config_logger()
    adjust_file(*ask_user_input())


if __name__ == "__main__":
    main()
