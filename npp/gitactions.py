#!/usr/bin/env python

import os
import re
import shutil
import subprocess
from subprocess import CalledProcessError


def get_git_username():
    cmd = 'git config user.name'
    try:
        p = subprocess.check_call(cmd.split())
    except CalledProcessError:
        p = ''
    return p.strip()


def get_git_email():
    cmd = 'git config user.email'
    try:
        p = subprocess.check_call(cmd.split())
    except CalledProcessError:
        p = ''
    return p.strip()


def init_git_repo():
    cmd = 'git init'
    try:
        p = subprocess.check_call(cmd.split())
    except CalledProcessError:
        return False
    else:
        return True


def add_repo_remote(remote, url):
    cmd = 'git remote add {r} {u}'.format(r=remote, u=url)
    try:
        p = subprocess.check_call(cmd.split())
    except CalledProcessError:
        return False
    else:
        return True


def set_repo_remote(remote, url):
    cmd = 'git remote set-url {r} {u}'.format(r=remote, u=url)
    try:
        p = subprocess.check_call(cmd.split())
    except CalledProcessError:
        return False
    else:
        return True


def git_pull_from_remote(remote, branch='master'):
    if git_fetch_from_remote(remote):
        return git_merge_from_remote(remote, branch)
    else:
        return False


def git_fetch_from_remote(remote):
    cmd = 'git fetch {}'.format(remote)
    try:
        p = subprocess.check_call(cmd.split())
    except CalledProcessError:
        return False
    else:
        return True


def git_merge_from_remote(remote, branch='master'):
    cmd = 'git merge {r}/{b} --ff-only'.format(r=remote, b=branch)
    try:
        p = subprocess.check_call(cmd.split())
    except CalledProcessError:
        return False
    else:
        return True
