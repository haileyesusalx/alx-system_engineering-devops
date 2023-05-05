#!/usr/bin/env ruby
import re

# Define regular expressions to match the relevant fields in the log lines
sender_pattern = r"\[from:([^]]+)\]"
receiver_pattern = r"\[to:([^]]+)\]"
flags_pattern = r"\[flags:([^]]+)\]"

# Open the log file for reading
with open("logfile.txt", "r") as f:
    # Iterate over each line in the file
    for line in f:
        # Use regular expressions to extract the sender, receiver, and flags
        sender_match = re.search(sender_pattern, line)
        receiver_match = re.search(receiver_pattern, line)
        flags_match = re.search(flags_pattern, line)

        # If all three fields were found, print them in the required format
        if sender_match and receiver_match and flags_match:
            sender = sender_match.group(1)
            receiver = receiver_match.group(1)
            flags = flags_match.group(1)
            print(f"{sender},{receiver},{flags}")
