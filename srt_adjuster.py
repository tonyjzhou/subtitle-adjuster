#!/usr/bin/env python3

from __future__ import print_function

from lib.args import get_args
from lib.files import adjust_file
from lib.log_config import config_logger
from lib.validators import validate


def main():
    config_logger()

    srt_original, seconds = get_args()

    validate(srt_original, seconds)

    adjust_file(srt_original, int(seconds))


if __name__ == "__main__":
    main()
