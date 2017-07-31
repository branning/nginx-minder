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

from datetime import datetime
import re
from sys import stdout
from time import sleep

from docopt import docopt

ACCESS_LOG = '/var/log/nginx/access.log'
BLANK_REPORT = {'200': 0,
                '300': 0,
                '400': 0,
                '500': 0,
                'routes': {}}
# read loglines produced by this nginx log_format directive
#log_format main '$remote_addr - $http_x_forwarded_for - $http_x_realip - '
#                '[$time_local] $scheme $http_x_forwarded_proto '
#                '"$request" $status '
#                '$body_bytes_sent "$http_referer" "$http_user_agent"';
LOG_REGEX = ('(\S+) - (\S+) - (\S+) - '
             '\[([^\]]+)\] (\S+) (\S+) '
             '"([^"]+)" (\S+) '
             '(\S+) "([^"]+)" "([^"]+)"')
# we compile this once, the log lines aren't expected to change format
log_scanner = re.compile(LOG_REGEX)

def log(report):
    print("50x:{}|s".format(report['500']))
    print("40x:{}|s".format(report['400']))
    print("30x:{}|s".format(report['300']))
    print("20x:{}|s".format(report['200']))
    for route, count in report['routes']:
        print("{}:{}|s".format(route, count))
    stdout.flush()

def parse_nginx_log(line):
    match = log_scanner.match(line)
    if not match:
        raise ValueError("failed to parse log line: {}".format(line))
    request = match.group(7)
    verb, route, protocol = request.split(' ')
    code = int(match.group(8))
    return code, route

def follow(filename):
    '''open a file and jump to the end, then yield all the lines that show up'''
    with open(filename, 'r') as f:
        f.seek(0, 2)  # go to the end
        while True:
            line = f.readline()
            yield line

def report(period):
    log_lines = follow(ACCESS_LOG)
    report = BLANK_REPORT.copy()
    log(report)
    now = datetime.now()
    then = now
    while True:
        # every time period, make a report and reset our counts
        now = datetime.now()
        elapsed = now - then
        if elapsed.seconds > period:
            then = now
            log(report)
            report = BLANK_REPORT.copy()
        line = next(log_lines)
        if not line:
            sleep(0.1) # don't spin-wait
            continue
        try:
            code, route = parse_nginx_log(line)
        except ValueError as e:
            print(e)
            continue
        bucket = str(int(code / 100) * 100)
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

