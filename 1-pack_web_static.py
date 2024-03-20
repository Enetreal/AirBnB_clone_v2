#!/usr/bin/python3
"""
Fabfile to generate a .tgz archive from the contents of web_static.
"""

import os.path
from datetime import datetime
from fabric.api import local

def do_pack():
    """Create a tar gzipped archive of the directory web_static."""
    dt = datetime.utcnow()
    file_name = "versions/web_static_{}{}{}{}{}{}.tgz".format(dt.year,
                                                             dt.month,
                                                             dt.day,
                                                             dt.hour,
                                                             dt.minute,
                                                             dt.second)
    if not os.path.isdir("versions"):
        local("mkdir -p versions")
    if local("tar -cvzf {} web_static".format(file_name)).failed:
        return None
    return file_name
