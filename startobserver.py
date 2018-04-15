#!/usr/bin/env python3

import os

import builder

RUN_INOTIFY_CMD = 'while inotifywait -r . -e modify -e move -e create -e delete; do ../builder.py; done'


class StartObserver:
    def __init__(self):
        builder.Builder()
        os.system(RUN_INOTIFY_CMD)


if __name__ == "__main__":
    StartObserver()