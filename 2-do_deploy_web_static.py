#!/usr/bin/python3
"""distributes an archive to your web servers, using the function do_deploy"""
from os.path import exists
import os
from fabric.api import env, put, run


env.hosts = ["104.196.123.117", "34.75.191.254"]


def do_deploy(archive_path):
    """distributes an archive to your web servers"""
    if (exists(archive_path) is True):
        try:
            path_releases = "/data/web_static/releases/"
            path_current = "/data/web_static/current"
            file = archive_path.split("/")[-1]
            ex = file.split(".")[0]
            put(archive_path, '/tmp/')
            run('sudo mkdir -p {}{}/'.format(path_releases, ex))
            run('sudo tar -xzf /tmp/{} -C {}{}/'
                .format(file, path_releases, ex))
            run('sudo rm /tmp/{}'.format(file))
            run('sudo mv {0}{1}/web_static/* {0}{1}/'
                .format(path_releases, ex))
            # here
            run('sudo rm -rf {}{}/web_static'.format(path_releases, ex))
            run('sudo rm -rf {}'.format(path_current))
            run('sudo ln -s {}{}/ {}'.format(path_releases, ex, path_current))
            return True
        except:
            return False
    return (False)
