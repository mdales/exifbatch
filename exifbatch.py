#!/usr/bin/env python

import os
import shutil
import subprocess
import sys

import pandas as pd

exclude_columns = ['shot', 'filename', 'targetfilename']

def main() -> None:
    df = pd.read_excel(sys.argv[1])
    photos_base_dir = sys.argv[2]
    target_dir = sys.argv[3]

    os.makedirs(target_dir, exist_ok=True)

    photos = os.listdir(photos_base_dir)
    for photo in photos:
        photopath = os.path.join(photos_base_dir, photo)

        row = df[df.filename==photo]
        data = row.to_dict(orient='records')[0]
        # print(data)

        targetfilename = data['targetfilename']
        if not targetfilename or not isinstance(targetfilename, str):
            targetfilename = photo
        targetpath = os.path.join(target_dir, targetfilename)

        shutil.copyfile(photopath, targetpath)

        if data['targetfilename']:
            print(['exiftool', '-alldates<filename', targetpath])
            subprocess.call(['exiftool', '-alldates<filename', targetpath])

        for key, value in data.items():
            if not key or not value or key in exclude_columns:
                continue
            print(['exiftool', targetpath, '-overwrite_original', f'-{key}={value}'])
            subprocess.call(['exiftool', targetpath, '-overwrite_original', f'-{key}={value}'])


if __name__ == "__main__":
    main()
