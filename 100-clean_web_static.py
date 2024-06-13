#!/usr/bin/python3
""" Fabric script that deletes out-of-date archives """
from fabric.api import *

env.hosts = ['18.204.9.11', '18.233.66.83']
env.user = "ubuntu"


def do_clean(number=0):
    """ Deletes out-of-date archives """

    number = 1 if int(number) == 0 else int(number)
    number += 1

    # Delete local archives except the most recent 'number' ones
    local('cd versions ; ls -t | tail -n +{} | xargs rm -rf'.format(number))

    # Delete remote archives except the most recent 'number' ones
    path = '/data/web_static/releases'
    run('cd {} ; ls -t | tail -n +{} | xargs rm -rf'.format(path, number))

