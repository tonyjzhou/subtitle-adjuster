#!/usr/bin/env python3

import logging
import os

from lib.line_adjuster import adjust


def adjust_file(srt_original, srt_new_path, seconds):
    backup_file_name = backup_original_file(srt_original)
    update_new_time(backup_file_name, seconds, srt_original)
    logging.info("Generated new srt as %s", srt_original)


def backup_original_file(srt_original):
    backup_file = make_backup_file(srt_original)
    os.rename(srt_original, backup_file)
    return backup_file


def update_new_time(backup_file_name, seconds, new_file_name):
    with open(backup_file_name, "r", encoding='utf-8') as orig_file:
        with open(new_file_name, "w", encoding='utf-8') as new_file:
            for line in orig_file.readlines():
                print(adjust(line, seconds), file=new_file)


def make_backup_file(srt_original):
    return srt_original + '.bak'


def is_valid_file_type(file_name):
    _, extension = os.path.splitext(file_name)
    return extension.lower() == '.srt'
