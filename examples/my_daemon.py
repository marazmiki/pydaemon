#!/usr/bin/env python
# coding: utf-8

from __future__ import print_function
import sys;sys.path.insert(0, '..')
import argparse
import pydaemon
import os
import time


class ExampleDaemon(pydaemon.Daemon):
    def run(self):
        """
        A long process
        """
        print("Do nothing")
        while True:
            time.sleep(0.1)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='ExampleDaemon runner',
        epilog='That\'s all folks')

    parser.add_argument('operation',
                    metavar='OPERATION',
                    type=str,
                    help='Operation with daemon. Accepts any of these values: start, stop, restart, status',
                    choices=['start', 'stop', 'restart', 'status'])
    args = parser.parse_args()
    operation = args.operation

    # Daemon
    cwd = os.path.abspath(os.path.dirname(__file__))
    pidfile = os.path.join(cwd, 'example_daemon.pid')

    daemon = ExampleDaemon(pidfile=pidfile)

    if operation == 'start':
        print("Starting daemon")
        daemon.start()
        pid = daemon.get_pid()

        if not pid:
            print("Unable run daemon")
        else:
            print("Daemon is running [PID=%d]" % pid)

    elif operation == 'stop':
        print("Stoping daemon")
        daemon.stop()

    elif operation == 'restart':
        print("Restarting daemon")
        daemon.restart()

    elif operation == 'status':
        print("Viewing daemon status")
        pid = daemon.get_pid()

        if not pid:
            print("Daemon isn't running ;)")
        else:
            print("Daemon is running [PID=%d]" % pid)
    sys.exit(0)

