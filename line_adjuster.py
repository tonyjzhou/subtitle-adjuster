import re

import datetime


def adjust(line, seconds):
    time_pattern = re.compile(r'\d\d:\d\d:\d\d,\d\d\d')

    if time_pattern.match(line):
        start, end = time_pattern.findall(line)
        return '{0} --> {1}'.format(adjust_time(seconds, start), adjust_time(seconds, end))
    else:
        return line.strip()


def adjust_time(seconds, time_string):
    time_format = "%H:%M:%S,%f"
    time = datetime.datetime.strptime(time_string, time_format)
    adjusted_time = time + datetime.timedelta(0, seconds)
    return adjusted_time.strftime(time_format).replace('000', '')
