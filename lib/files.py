#!/usr/bin/env python3

import logging
import os
from lib.line_adjuster import adjust


def adjust_file(srt_original, srt_new_path, seconds):
    srt_new = make_srt_new(srt_new_path, srt_original)

    with open(srt_original, "r", encoding='utf-8') as orig_file:
        with open(srt_new, "w", encoding='utf-8') as new_file:
            for line in orig_file.readlines():
                print(adjust(line, seconds), file=new_file)

    logging.info("Generated new srt as %s", srt_new)


def make_srt_new(srt_new_path, srt_original):
    srt_new_file_base_name = make_new_base_name(srt_original)
    srt_new = os.path.join(srt_new_path, srt_new_file_base_name)
    return srt_new


def make_new_base_name(srt_original):
    basename = os.path.basename(srt_original)
    first, second = os.path.splitext(basename)
    return first + '.new' + second


def is_valid_file_type(file_name):
    _, extension = os.path.splitext(file_name)
    return extension.lower() == '.srt'
