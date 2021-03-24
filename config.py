import os
import logging


CAMERA = os.getenv("CAMERA")
SEAWEED_URL = os.getenv("SEAWEED_URL")


logging.basicConfig(format="%(asctime)8s %(levelname)-8s %(message)s")
logger: logging.Logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)