#!/usr/bin/env python3

'''
nginx-minder - nginx access log watcher and reporter

Usage:
    nginx-minder.py [--period=<s>]
    nginx-minder.py -h | --help
    nginx-minder.py --version

Options:
    --period=<s>     Reporting period in seconds [default: 5]
    -h --help        Show this message
    --version        Show version
'''

import asyncio
from datetime import datetime
from time import sleep

from docopt import docopt

ACCESS_LOG = '/var/log/nginx/access.log'
# TODO: use Counter
BLANK_REPORT = {'200': 0,
                '300': 0,
                '400': 0,
                '500': 0,
                'routes': {}}

def log(report):
    print("50x:{}|s".format(report['500']))
    print("40x:{}|s".format(report['400']))
    print("30x:{}|s".format(report['300']))
    print("20x:{}|s".format(report['200']))
    for route, count in report['routes']:
        print("{}:{}|s".format(route, count))

def parse_nginx_log(line):
    code = 200
    route = None
    return code, route

def follow(filename):
    '''open a file and jump to the end, then yield all the lines that show up'''
    with open(filename, 'r') as f:
        f.seek(0, 2)  # go to the end
        while True:
            line = f.readline()
            if not line:
                sleep(0.1) # don't spin-wait
                continue
            yield line

def report(period):
    report = BLANK_REPORT
    log(report)
    now = datetime.now()
    while True:
        # every time period, make a report and reset our counts
        then = now
        now = datetime.now()
        elapsed = now - then
        if elapsed.seconds > period:
            log(report)
            report = BLANK_REPORT
        code, route = parse_nginx_log(follow(ACCESS_LOG))
        bucket = str(int(code / 100 * 100))
        report[bucket] += 1
        # if there was an error, make a note of the route, too
        if bucket == '500':
            try:
                report['routes'][route] += 1
            except KeyError:
                report['routes'][route] = 1


if __name__=='__main__':
    arguments = docopt(__doc__, version='nginx-minder 1.0')
    report(int(arguments['--period']))
