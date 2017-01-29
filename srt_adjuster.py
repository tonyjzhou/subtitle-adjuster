#!/usr/bin/env python3

from __future__ import print_function

import logging
import os
import os.path

from lib.line_adjuster import adjust
from lib.log_config import config_logger


def adjust_file(srt_original, srt_new, seconds):
    with open(srt_original, "r", encoding='utf-8') as orig_file:
        with open(srt_new, "w", encoding='utf-8') as new_file:
            for line in orig_file.readlines():
                print(adjust(line, seconds), file=new_file)
    logging.info("Generated new srt as %s", srt_new)


def make_new_base_name(srt_original):
    basename = os.path.basename(srt_original)
    first, second = os.path.splitext(basename)
    return first + '.new' + second


def ask_user_input():
    srt_original = ask_valid_original_file_name()
    srt_new = ask_valid_new_path_name(make_new_base_name(srt_original))
    seconds = input('Enter seconds to add to or remove from (negative number) original srt (e.g. 1 or -1): ')

    logging.debug("srt_original=%s", srt_original)
    logging.debug("srt_new=%s", srt_new)
    logging.debug("seconds=%s", seconds)

    return srt_original, srt_new, seconds


def ask_valid_new_path_name(srt_new_file_base_name):
    while True:
        path_name = input('Enter path for the new srt file (e.g. /Users/tonyzhou/Movies): ')

        if os.path.isdir(path_name):
            srt_new_file_name = os.path.join(path_name, srt_new_file_base_name)
            if not os.path.exists(srt_new_file_name):
                return srt_new_file_name
            else:
                print('"%s" already exists\nPlease try again ...\n' % srt_new_file_name)
        else:
            print('Invalid new path: "%s"\nPlease try again ...\n' % path_name)


def is_valid_file_type(file_name):
    _, extension = os.path.splitext(file_name)
    return extension.lower() == '.srt'


def ask_valid_original_file_name():
    while True:
        file_name = input('Enter full srt original file path (e.g. /Users/tonyzhou/Movies/abc.srt): ')

        if os.path.isfile(file_name) and is_valid_file_type(file_name):
            return file_name
        else:
            print('Invalid original file: "%s"\n' % file_name)


def main():
    config_logger()
    adjust_file(*ask_user_input())


if __name__ == "__main__":
    main()
