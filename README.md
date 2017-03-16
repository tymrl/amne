# Amne Engineering Challenge

This is a solution to the engineering problem here: https://www.amne.co/challenge/ .  It was written in Python 3.5.1 on macOS 10.12.2.

## Requirements

A Python 3.5 virtual environment with numpy and nose installed.  N.B. I tried it with Python 3.4 and ran into an "array is too big" error from numpy.

## Instructions

`range_counter.py` is configured as a command line tool using argparse.  Simply use

```
python range_counter.py /path/to/input/file.txt
```

To test, just run `nosetests` within the directory.
