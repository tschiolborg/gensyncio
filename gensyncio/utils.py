import time

from gensyncio.event import EventLoop


def sleep(seconds):
    start = time.time()
    while time.time() < start + seconds:
        yield


def gather(*tasks):
    loop = EventLoop()
    for task in tasks:
        loop.create_task(task)

    yield loop.run_forever()
