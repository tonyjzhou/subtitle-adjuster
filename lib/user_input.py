#!/usr/bin/env python3
import logging

from lib.validators import validate_srt_file


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

        if validate_srt_file(file_name):
            return file_name
        else:
            print('\n\tInvalid original file: "%s"\n\tPlease try again ...\n' % file_name)


def quit_gracefully():
    print('Bye')
