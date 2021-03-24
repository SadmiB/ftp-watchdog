import os
from inotify_simple import INotify, flags
import time

import utils
from config import SEAWEED_URL, CAMERA, logger


if __name__ == "__main__":
    logger.info("Starting...")
    inotify = INotify()
    watch_flags = flags.CREATE
    dir_path = '/home/ftpuser/' + CAMERA
    wd = inotify.add_watch(dir_path, watch_flags)
    logger.info(f"Watching {dir_path}..")
    while True:
        for event in inotify.read():
            logger.info(event)
            image = event.name
            time.sleep(60)
            if image[-4:] == ".jpg":
                utils.store_seaweed_snapshot(SEAWEED_URL, CAMERA, image)

