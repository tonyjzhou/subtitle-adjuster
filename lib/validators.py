#!/usr/bin/env python3
import logging
import os


def validate(srt_original, seconds):
    if not validate_srt_file(srt_original):
        logging.error('Invalid original file: "%s"', srt_original)
        exit(0)
    if not validate_seconds(seconds):
        logging.error('Invalid integer value for seconds: "%s"', seconds)
        exit(0)


def is_valid_file_type(file_name):
    _, extension = os.path.splitext(file_name)
    return extension.lower() == '.srt'


def validate_srt_file(file_name):
    return os.path.isfile(file_name) and is_valid_file_type(file_name)


def validate_seconds(value):
    try:
        int(value)
        return True
    except ValueError:
        return False
