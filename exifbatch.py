#!/usr/bin/env python

import subprocess
import sys

FILENAME_BASE = 1

lines = []
with open(sys.argv[1]) as f:
    lines = f.readlines()

# first line gives us the exif keys
exifbits = lines[0].strip().split(',')
lines = lines[1:]

for line in lines:
    bits = line.strip().split(',')
    joined = zip(bits, exifbits)
    filename = bits[1]
    print(f"Processing {filename}")
    for item in joined:
        if not item[0] or not item[1] or item[1] in ['filename', 'shot']:
            continue
        subprocess.call(['exiftool', filename, '-overwrite_original', f'-{item[1]}={item[0]}'])
        # print(['exiftool', filename, '-overwrite_original', f'-{item[1]}={item[0]}'])
