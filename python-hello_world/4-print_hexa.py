#!/usr/bin/python3
# Iterate through numbers from 0 to 98 (inclusive)
for i in range(99):
    # Print the current number in decimal and hexadecimal formats
    # {:d} is replaced by the decimal representation of the number
    # {:x} is replaced by the lowercase hexadecimal representation of the number
    print("{:d} = 0x{:x}".format(i, i))
