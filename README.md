## History:

Did you ever wonder how many system calls ran in less than a second? If yes, you are not alone. I had a scenario to know the number of write calls in less than 500 microseconds. That was the moment, for the birth of this script.

This script provides the number of calls per duration. Also this script is designed to be used for times from strace -ttt.

## Usage:

Below command traces read calls per 250 microsecond interval for a running process 23456
> strace -ttt -e trace=read -p 23456 2>&1 >/dev/null | ./count.py 0.000250

Below command traces write calls per 250 microsecond interval for dd command
> strace -ttt -e trace=write dd if=/dev/zero of=/data/output.1 bs=1K count=100000 2>&1 >/dev/null | ./count.py 0.000250
