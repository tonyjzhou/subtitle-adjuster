#!/usr/bin/env python3

from __future__ import print_function

from lib.files import adjust_file
from lib.log_config import config_logger
from lib.user_input import ask_user_input, quit_gracefully


def main():
    config_logger()

    try:
        adjust_file(*ask_user_input())
    except EOFError:
        quit_gracefully()


if __name__ == "__main__":
    main()
