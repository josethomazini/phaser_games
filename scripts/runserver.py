#!/usr/bin/env python3

import os

RUN_SERVER_CMD = 'python -m SimpleHTTPServer 8080'

class RunServer:
    def __init__(self):
        os.system(RUN_SERVER_CMD)


if __name__ == "__main__":
    RunServer()
