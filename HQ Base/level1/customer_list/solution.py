#!/usr/bin/env python3

from string import ascii_lowercase


message = "20 8 5 19 5 3 18 5 20 9 19 23 8 5 5 12".split(" ")
sol = ""
for l in message:
    sol += ascii_lowercase[int(l)-1]
print(sol)
