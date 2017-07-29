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

from docopt import docopt

if __name__=='__main__':
    arguments = docopt(__doc__, version='nginx-minder 1.0')
    print(arguments)

