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

from time import sleep

from docopt import docopt

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

if __name__=='__main__':
    arguments = docopt(__doc__, version='nginx-minder 1.0')
    print(arguments)

