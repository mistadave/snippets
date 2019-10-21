from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import os
import json
import time


class MoveHander(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(folder_to_track):
            src = folder_to_track + '/' + filename
            new_dest = folder_dest + '/' + filename
            os.rename(src, new_dest)


folder_to_track = '/tmp/track'
folder_dest = '/tmp/dest'


def run():
    event_handler = MoveHander()
    observer = Observer()
    observer.schedule(event_handler, folder_to_track, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(10)
    except KeyboardInterrupt as err:
        observer.stop()
        print('abort program: {}'.format(err))
    observer.join()


if __name__ == "__main__":
    run()
