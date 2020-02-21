import requests
import json

import settings
from packaging import version
import logging
import tarfile
import shutil, os
import time

logging.basicConfig(
        filename="log.log",
        format='%(asctime)s %(message)s', 
        datefmt='%m/%d/%Y %I:%M:%S %p', 
        level=logging.INFO)

def main():
    """Check if there is a need to update the data."""
    resp = requests.get(settings.VERSION)
    data = json.loads(resp.content)
    newest = data[0]
    if not settings.LATEST:
        logging.info("No version yet, updating!")
        update(newest)

    elif version.parse(newest) > version.parse(settings.LATEST):
        logging.info("Found newer version. updating!")
        update(newest)
    else:
        logging.info("No updated version found.")



def update(version):
    """Update the datafiles."""
    
    # Download File
    url = settings.TAIL % version
    data = requests.get(url)
    logging.info(data.content)
    with open("latest.tgz", "wb+") as datafile:
        datafile.write(data.content)
    logging.info("Downloaded static files.")

    # Deleting data folder
    shutil.rmtree('./static_files')
    os.mkdir('./static_files')
    members = [version, "img"]
    tar = tarfile.open("latest.tgz", "r:gz")
    tar.extractall(members, "./static_files/")
    tar.close()
    logging.info("Extracted static files.")
    os.rename(version, "data")

    if settings.JENKINS_HOOK:
        requests.get(settings.JENKINS_HOOK)

main()
