#!/usr/bin/env python3
import os


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
