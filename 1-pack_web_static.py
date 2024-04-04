#!/usr/bin/python3
"""1. Compress before sending"""

from fabric.api import local
from datetime import datetime


def do_pack():
    """
    Compresses the contents of the web_static folder into a tgz archive.
    """
    try:
        current_time = datetime.now().strftime("%Y%m%d%H%M%S")
        archive_path = "versions/web_static_{}.tgz".format(current_time)
        local("mkdir -p versions")
        local("tar -czvf {} web_static".format(archive_path))
        return archive_path
    except Exception as e:
        print("Error packing the archive: {}".format(e))
        return None
