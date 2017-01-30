#!/usr/bin/env python3

import logging
import os

from lib.line_adjuster import adjust


def adjust_file(srt_original, seconds):
    backup_file_name = make_backup_file(srt_original)
    os.rename(srt_original, backup_file_name)
    logging.debug("Generated backup file as %s", backup_file_name)
    update_new_time(backup_file_name, seconds, srt_original)
    logging.info("Adjusted the time by %d seconds in %s", seconds, srt_original)


def update_new_time(backup_file_name, seconds, new_file_name):
    with open(backup_file_name, "r", encoding='utf-8') as orig_file:
        with open(new_file_name, "w", encoding='utf-8') as new_file:
            for line in orig_file.readlines():
                print(adjust(line, seconds), file=new_file)


def make_backup_file(srt_original):
    return srt_original + '.bak'


