#!/usr/bin/python3

import datetime
today = datetime.datetime.now()
# print(str(today))
# print(repr(today))
time = repr(today)

print(eval(time) == today)
