#!/usr/bin/env python

""" Wrappers around git command line calls. """

import os
import re
import shutil
import subprocess
from subprocess import CalledProcessError


def get_git_username():
    """ Get the git username from the git config. return empty string if not success. """
    cmd = 'git config user.name'
    try:
        p = subprocess.check_call(cmd.split())
    except CalledProcessError:
        p = ''
    return p.strip()


def get_git_email():
    """ Get the git user email from the git config. return empty string if not success. """
    cmd = 'git config user.email'
    try:
        p = subprocess.check_call(cmd.split())
    except CalledProcessError:
        p = ''
    return p.strip()


def init_git_repo():
    """ Initialize a bare git repo in the current directory. Return True/False based on success. """
    cmd = 'git init'
    try:
        p = subprocess.check_call(cmd.split())
    except CalledProcessError:
        return False
    else:
        return True


def add_repo_remote(remote, url):
    """ Add a remote to a repo in the current directory. Return True/False on success. """
    cmd = 'git remote add {r} {u}'.format(r=remote, u=url)
    try:
        p = subprocess.check_call(cmd.split())
    except CalledProcessError:
        return False
    else:
        return True


def set_repo_remote(remote, url):
    """ Set the url of an existing remote. Return True/False on success. """
    cmd = 'git remote set-url {r} {u}'.format(r=remote, u=url)
    try:
        p = subprocess.check_call(cmd.split())
    except CalledProcessError:
        return False
    else:
        return True


def git_pull_from_remote(remote, branch='master'):
    """ Fetch and merge from the specified remote and branch. Return True/False on success. """
    if git_fetch_from_remote(remote):
        return git_merge_from_remote(remote, branch)
    else:
        return False


def git_fetch_from_remote(remote):
    """ Fetch from the specified remote. Return True/False on success. """
    cmd = 'git fetch {}'.format(remote)
    try:
        p = subprocess.check_call(cmd.split())
    except CalledProcessError:
        return False
    else:
        return True


def git_merge_from_remote(remote, branch='master'):
    """ Merge the specified remote/branch only if it can be fast forwarded. Return True/False on success. """
    cmd = 'git merge {r}/{b} --ff-only'.format(r=remote, b=branch)
    try:
        p = subprocess.check_call(cmd.split())
    except CalledProcessError:
        return False
    else:
        return True
