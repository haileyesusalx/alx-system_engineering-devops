#!/usr/bin/env python3

import sys
import re

log_file = sys.argv[1]

with open(log_file) as f:
    for line in f:
        match = re.search(r"\[from:(.*?)\] \[to:(.*?)\] \[flags:(.*?)\]", line)
        if match:
            sender = match.group(1)
            receiver = match.group(2)
            flags = match.group(3)
            print(f"{sender},{receiver},{flags}")
