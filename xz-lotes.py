#!/usr/bin/python
import os, time, glob, subprocess

files = glob.glob('*.raw') + glob.glob('*.img')

workers = []
while files or workers:
    while len(workers) < 4 and files:
        f = files[0]
        files = files[1:]
        w = subprocess.Popen(['xz', f,
            os.path.splitext(f)[0]])
        workers.append(w)
    for w in list(workers):
        if w.poll() is not None:
            workers.remove(w)
    time.sleep(0.1)
