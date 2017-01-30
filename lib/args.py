#!/usr/bin/env python3
import argparse


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("srt_original", help="the full file name of the srt (e.g. /Users/tonyzhou/Movies/abc.srt)")
    parser.add_argument("seconds", help="the number of seconds to be adjusted (e.g. 1 or -1)")
    args = parser.parse_args()
    return args.srt_original, args.seconds
