import asyncio
import logging
import os
from time import sleep
from threading import Event

import forklib


logging.basicConfig(level=logging.DEBUG)


def run():
    print(
        "Proceess #{id} has PID: {pid}".format(
            id=forklib.get_id(),
            pid=os.getpid(),
        ),
    )
    sleep(3)


exit_event = Event()


def thread_callback():
    while not exit_event.is_set():
        sleep(0.5)
        print("Thread callback making great stuff")
    print("Thread callback finished")


async def async_callback():
    await asyncio.sleep(5)
    print("Async callback finished")


def main():
    print("Master proccess has PID: {0}".format(os.getpid()))
    forklib.fork(
        4, run,
        thread_callback=thread_callback,

        # Wait theread_callback, otherwise exit (default)
        # Note: You have to be careful when using this option.
        # Thread cancellation is impossible in the general case and you must
        # implement your own way of thread exit notification for example
        # like following one using exit_callback and threading.Event
        wait_thread_callback=True,

        # Notifying thread_callback about exit.
        exit_callback=exit_event.set,

        async_callback=async_callback,
        # Wait async_callback, otherwise cancel incomplete tasks (default)
        wait_async_callback=True
    )


if __name__ == "__main__":
    main()