import time

import gensyncio


loop = gensyncio.EventLoop()


def hello():
    print("Hello")
    yield from gensyncio.sleep(0.5)
    print("World")


def main():
    bef = time.time()

    yield from gensyncio.gather(hello(), hello(), hello())

    print(time.time() - bef)


loop.create_task(main())
loop.run_forever()
