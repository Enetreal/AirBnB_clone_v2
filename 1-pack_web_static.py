#!/usr/bin/python3
<<<<<<< HEAD
"""Generates .tgz archive from contents of the web_static folder"""


from datetime import datetime
from fabric.api import local
import os


def do_pack():
    """Creates a .tgz archive"""
    dt_stamp = datetime.utcnow()
    output = "versions/web_static_{}{}{}{}{}{}.tgz".format(
        dt_stamp.year,
        dt_stamp.month,
        dt_stamp.day,
        dt_stamp.hour,
        dt_stamp.minute,
        dt_stamp.second
    )

    if not os.path.exists('versions'):
        os.makedirs('versions')

    res = local("tar -cvzf {} web_static".format(output))
    if res.failed:
        return None

    return output
=======
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
>>>>>>> ca44d7a789ba744a1ff57ace8f91fd998aeae4ba
