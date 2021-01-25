#!/usr/bin/python3
"""creates and distributes an archive to your web servers"""
from fabric.api import local
import time
from fabric.api import run, put, env
from os.path import exists


env.hosts = ['35.243.242.25', '34.75.82.34']


def do_pack():
    """function do_pack"""

    local("mkdir -p versions")
    created = (time.strftime("%Y%m%d%H%M%S"))
    tgzfile = local("tar -cvzf versions/web_static_{}.tgz web_static"
                    .format(created))
    if not tgzfile.succeeded:
        return None
    else:
        return "versions/web_static_{}.tgz".format(created)


def do_deploy(archive_path):
    """creates and distributes an archive to your web servers"""
    if exists(archive_path) is True:
        try:
            filename = archive_path.split('/')[-1]
            no_ex = filename.split('.')[0]
            put(archive_path, '/tmp/')
            foldername = "/data/web_static/releases/" + no_ex
            run("mkdir -p {}/".format(foldername))
            run("tar -xzf /tmp/{} -C {}/".format(filename, foldername))
            run("rm  /tmp/{}".format(filename))
            run('mv {}/web_static/* {}/'.format(foldername, foldername))
            run("rm -rf {}/web_static".format(foldername))
            run("rm -rf /data/web_static/current")
            run("ln -s {}/\
                /data/web_static/current".format(foldername))
            return True
        except:
            return False
    return False


def deploy():
    """function deploy"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    else:
        call_dep = do_deploy(archive_path)
    return call_dep
