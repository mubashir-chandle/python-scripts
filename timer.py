#!/usr/bin/python3
# 2020-07-10
'''Timer with bell alert (only works on Linux).'''

import os
import time
import argparse
import sys

if sys.platform != 'linux':
    print('Oops, the program is only compatible with Linux systems :(')
    sys.exit(1)

parser = argparse.ArgumentParser()
parser.add_argument('seconds', help='number of seconds for which the timer should run', type=int)
parser.add_argument('-a',
                    '--alerts',
                    help='number of alert bells to produce after timer runs out',
                    type=int,
                    default=3,
                    choices=range(0, 6))

args = parser.parse_args()
seconds = args.seconds
alerts = args.alerts

if seconds < 0:
    print("Oops. Unfortunately the programmer was not very intelligent and didn't",
          "know how to write code for a timer that runs for negative seconds.",
          "As such, this feature is not available :(",
          sep='\n')
    sys.exit(1)

for i in range(seconds, 0, -1):
    if i == 1:
        print(f'{i} second  remaining')
    else:
        print(f'{i} seconds remaining')
    time.sleep(1)

print('Done :)')
for i in range(alerts):
    os.system(r'echo -ne "\a"')
    time.sleep(.5)
