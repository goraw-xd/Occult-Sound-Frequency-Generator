"""Async ritual execution queue placeholder."""

from queue import Queue

queue = Queue()

def enqueue(task):
    queue.put(task)
