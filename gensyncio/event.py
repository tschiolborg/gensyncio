from typing import Generator
import uuid


class Task:
    def __init__(self, gen: Generator):
        self._gen = gen
        self._is_done = False

    def step(self):
        try:
            next(self._gen)
        except StopIteration:
            self._is_done = True

    def is_done(self):
        return self._is_done


class EventLoop:
    _tasks: dict[uuid.UUID, Task]

    def __init__(self):
        self._tasks = {}

    def add_task(self, task: Task):
        self._tasks[uuid.uuid4()] = task

    def create_task(self, gen: Generator):
        self.add_task(Task(gen))

    def run_forever(self):
        while True:
            to_remove = []

            if not self._tasks:
                break

            for key, task in self._tasks.items():
                task.step()
                if task.is_done():
                    to_remove.append(key)

            for key in to_remove:
                del self._tasks[key]
