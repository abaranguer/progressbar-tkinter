#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import threading
import queue

class BackgroundJob(threading.Thread):
    queue = None

    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue

    def run(self):
        value = 0
        while value < 1000000:
            value = value + 1
            if value % 100000 == 0:
                self.queue.put(value)
                print("value %d" % (value))
             




