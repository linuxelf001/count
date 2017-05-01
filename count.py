#!/usr/bin/env python
import fileinput
import sys
import math
import re

if len(sys.argv) != 2:
        print("Requires one argument: interval (decimals allowed)")
        sys.exit(1)

interval = float(sys.argv[1])
if interval <= 0:
        print("Interval must be positive")
        sys.exit(1)

pattern = re.compile(r"[ \t]")

last = float("NaN")
nxt = float("NaN")
cnt = 0
for line in fileinput.input("-"):
        num = float("NaN")
        try:
                num = float(pattern.split(line.strip())[0])
        except ValueError:
                continue
        if math.isnan(last):
                cnt = 1
                last = num
                nxt = num + interval
        elif num < last:
                continue
        while num >= nxt:
                print("{0:.6f}\t{1}".format(last, cnt))
                cnt = 0
                last = nxt
                nxt += interval
        cnt += 1

print("{0:.6f}\t{1}".format(last, cnt))
