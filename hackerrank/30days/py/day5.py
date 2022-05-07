#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    x = 1
    while x < 11:
        print(f"{n} x {x} = {n*x} ")
        x += 1