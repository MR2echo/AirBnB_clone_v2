#!/usr/bin/python3
""" Fabric script that generates a .tgz archive
    from the contents of the web_static folder
"""
from fabric.api import local
import os
from datetime import datetime


def do_pack():
    """ generates the archive """

    if not os.path.exists('versions'):
        local('mkdir versions')

    d = datetime.utcnow()

    file_path = "versions/web_static_{}.tgz".format(d.strftime("%Y%m%d%H%M%S"))

    result = local('tar -cvzf {} web_static'.format(file_path))

    if result.failed:
        return None
    else:
        return file_path

