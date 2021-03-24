import os
import requests
from config import logger

def store_seaweed_snapshot(camera, seaweed_url , image):

    year = image[0:4]
    month = image[4:6]
    day = image[6:8]
    hour = image[9:11]
    minute = image[11:13]
    second = image[13:15]

    logger.info("Uploading image {image}..")
    
    snapshot = minute + "_" + second + "_000.jpg"

    url = seaweed_url + \
        camera + "/snapshots/recordings" + \
        "/" + year + "/" + month + "/" + day + "/" + hour + "/" + snapshot
    logger.info("Url {url}..")
    image_content = open("/home/ftpuser/" + camera + "/" + image, 'rb')
    files = {'file': image_content}
    
    try:
        response = requests.post(url, files=files)
        logger.info(f"Response {response}..")
    except Exception as e:
        logger.info(f"Something went wrong {e}..")
    finally:
        image_content.close()

def upload_dir_images(camera, seaweed_url ,image):
    images = os.listdir(image)
    for image in images:
        if image[-4:] == "jpg":
            store_seaweed_snapshot(camera, seaweed_url, image)

