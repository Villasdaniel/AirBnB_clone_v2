#!/usr/bin/python3
"""
generates a .tgz archive from the
contents of the web_static folder of your AirBnB
Clone repo, using the function do_pack
"""
from fabric.api import local
import time


def do_pack():
    """ for generate .tgz """

    local("mkdir -p versions")
    created = (time.strftime("%Y%m%d%H%M%S"))
    tgzfile = local("tar -cvzf versions/web_static_{}.tgz web_static"
                    .format(created))
    if not tgzfile.succeeded:
        return None
    else:
        return "versions/web_static_{}.tgz".format(created)
