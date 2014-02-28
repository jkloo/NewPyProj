#!/usr/bin/env python

import os
import re
import shutil
import subprocess
from subprocess import CalledProcessError


def fixup_project(name):
    proj_root = os.path.join(os.getcwd(), name)
    for root, dirs, files in os.walk(proj_root):
        dirs[:] = [d for d in dirs if d not in ['.git']]
        for f in files:
            if f.startswith('Foobar'):
                old = f
                f = re.sub('Foobar', name, f)
                os.rename(os.path.join(root, old), os.path.join(root, f))
            with open(os.path.join(root, f), 'r') as g:
                t = g.read()
            with open(os.path.join(root, f), 'w') as g:
                g.write(re.sub('Foobar', name, t))



def fixup_package(proj, name):
    proj_root = os.path.join(os.getcwd(), proj)
    package_root = os.path.join(proj_root, name)
    old_pack_root = os.path.join(proj_root, 'foobar')
    shutil.move(old_pack_root, package_root)
    for root, dirs, files in os.walk(proj_root):
        dirs[:] = [d for d in dirs if d not in ['.git']]
        for f in files:
            if f.startswith('foobar'):
                old = f
                f = re.sub('foobar', name, f)
                os.rename(os.path.join(root, old), os.path.join(root, f))
            t = ''
            with open(os.path.join(root, f), 'r') as g:
                t = g.read()
            with open(os.path.join(root, f), 'w') as g:
                g.write(re.sub('foobar', name, t))


def fixup_extras():
    pass


def _get_git_username():
    cmd = 'git config user.name'
    try:
        p = subprocess.check_call(cmd.split())
    except CalledProcessError:
        p = ''
    return p.strip()


def _get_git_email():
    cmd = 'git config user.email'
    try:
        p = subprocess.check_call(cmd.split())
    except CalledProcessError:
        p = ''
    return p.strip()


def _init_git_repo():
    cmd = 'git init'
    try:
        p = subprocess.check_call(cmd.split())
    except CalledProcessError:
        return False
    else:
        return True


def _add_repo_remote(remote, url):
    cmd = 'git remote add {r} {u}'.format(r=remote, u=url)
    try:
        p = subprocess.check_call(cmd.split())
    except CalledProcessError:
        return False
    else:
        return True


def _git_pull_from_remote(remote, branch='master'):
    if _git_fetch_from_remote(remote):
        return _git_merge_from_remote(remote, branch)
    else:
        return False


def _git_fetch_from_remote(remote):    
    cmd = 'git fetch {}'.format(remote)
    try:
        p = subprocess.check_call(cmd.split())
    except CalledProcessError:
        return False
    else:
        return True


def _git_merge_from_remote(remote, branch='master'):
    cmd = 'git merge {r}/{b} --ff-only'.format(r=remote, b=branch)
    try:
        p = subprocess.check_call(cmd.split())
    except CalledProcessError:
        return False
    else:
        return True
