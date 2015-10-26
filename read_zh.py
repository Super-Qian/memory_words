#!/usr/bin/env python
# coding=utf-8
import re
import os
file = raw_input('File name is:')
with open(file, 'rt') as f:
    for line in f:
        for char in line:
            if re.match(' ', char):
                n = line.index(char) + 1
        ss = line[n:]
        english = line[:n - 1]
        print ss,
        input = raw_input('input->')
        if input == english:
            espeak = 'espeak -s 130 ' + english
            os.system(espeak)
            print '>>Right\n'
        else:
            print '>>Wrong\n'
            if re.match('[q|Q]', input):
                break
            elif input == 'out':
                print english
