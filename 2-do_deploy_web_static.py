#!/usr/bin/python3
"""Compress web static package
"""
from fabric.api import put, run, env
from datetime import datetime
from os import path
from fabric.contrib.files import exists


env.hosts = ['100.25.167.16', '52.201.165.125']


def do_deploy(archive_path):
    """
    Distributes an archive to the web servers.
    """
    if not exists(archive_path):
        return False

    try:
        # Upload the archive to the /tmp/ directory of the web server
        put(archive_path, '/tmp/')

        # Get the archive filename without extension
        archive_filename = archive_path.split('/')[-1]
        archive_folder = archive_filename.split('.')[0]

        # Uncompress the archive to the folder /data/web_static/releases/<archive filename without extension>
        run('mkdir -p /data/web_static/releases/{}/'.format(archive_folder))
        run('tar -xzf /tmp/{} -C /data/web_static/releases/{}/'
            .format(archive_filename, archive_folder))

        # Delete the archive from the web server
        run('rm /tmp/{}'.format(archive_filename))

        # Move the contents of the uncompressed folder to the parent directory
        run('mv /data/web_static/releases/{}/web_static/* /data/web_static/releases/{}/'
            .format(archive_folder, archive_folder))

        # Remove the now empty web_static folder
        run('rm -rf /data/web_static/releases/{}/web_static'.format(archive_folder))

        # Delete the symbolic link /data/web_static/current from the web server
        run('rm -rf /data/web_static/current')

        # Create a new symbolic link /data/web_static/current linked to the new version
        run('ln -s /data/web_static/releases/{}/ /data/web_static/current'
            .format(archive_folder))

        return True
    except Exception as e:
        print("Error deploying the archive: {}".format(e))
        return False
