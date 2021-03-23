
import os
import requests
import logging

SEAWEED_URL = os.environ["SEAWEED_URL"] | "http://188.40.18.217:8888"
CAMERA = os.environ["CAMERA"]  | "dslrf-bxtgj"

def store_seaweed_snapshot(image):

    year = image[0:4]
    month = image[5:7]
    day = image[8:10]
    hour = image[11:13]
    minute = image[13:15]
    second = image[15:17]
    snapshot = minute + "_" + second + "_000.jpg"

    url = SEAWEED_URL + \
        str(CAMERA) + "/snapshots/recordings/" + \
        "/" + year + "/" + month + "/" + day + "/" + hour + "/" + snapshot

    image_content = open("/home/ftpuser/" + image, 'rb')
    files = {'file': image_content}
    
    try:
        r = requests.post(url, files=files)
        logging.debug(r)
    finally:
        image_content.close()

    
