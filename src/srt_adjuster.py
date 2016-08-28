from __future__ import print_function
import os

from line_adjuster import adjust


def make_new_filename(filename):
    base, extension = os.path.splitext(filename)
    return '{0}_new{1}'.format(base, extension)


def adjust_file(filename, seconds):
    new_filename = make_new_filename(filename)

    srt_file = open(filename, "r")
    new_file = open(new_filename, "w")

    for line in srt_file.readlines():
        print(adjust(line, seconds), file=new_file)


def main():
    adjust_file("srt/Silicon.Valley.S03E08.1080p.WEB.HEVC.2CH.x265.srt", -5)


if __name__ == "__main__":
    main()
