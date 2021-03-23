

import os
from inotify_simple import INotify, flags
import logging

import utils

inotify = INotify()
watch_flags = flags.CREATE
wd = inotify.add_watch('/svr/ftp', watch_flags)

while True:
    for event in inotify.read():
        print(event)
        image = event.name
        utils.store_seaweed_snapshot(image)
        
        

