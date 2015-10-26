#!/usr/bin/env python
# coding=utf-8
import re
import os
file = raw_input('File name:')
with open(file, 'rt') as f:
    for line in f:
        ss = ''
        for char in line:
            if re.match(' ', char):
                n = line.index(char) + 1
                break
            if re.match('[a-zA-Z]', char):
                ss += char
        print ss
        espeak = 'espeak -s 130 ' + ss
        os.system(espeak)
        input = raw_input('zh:output Chinese|q:quit>>>')
        if input == 'zh':
            zh = line[n:]
            print zh
        elif re.match('[q|Q]', input):
            break
