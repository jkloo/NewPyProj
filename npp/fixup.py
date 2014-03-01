#!/usr/bin/env python

import os
import re
import shutil
import subprocess
from subprocess import CalledProcessError


def fixup_project(project):
    proj_root = os.path.join(os.getcwd(), project)
    for root, dirs, files in os.walk(proj_root):
        dirs[:] = [d for d in dirs if d not in ['.git']]
        for f in files:
            if f.startswith('Foobar'):
                old = f
                f = re.sub('Foobar', project, f)
                os.rename(os.path.join(root, old), os.path.join(root, f))
            with open(os.path.join(root, f), 'r') as g:
                t = g.read()
            with open(os.path.join(root, f), 'w') as g:
                g.write(re.sub('Foobar', project, t))


def fixup_package(project, package):
    project_root = os.path.join(os.getcwd(), project)
    package_root = os.path.join(project_root, package)
    old_pack_root = os.path.join(project_root, 'foobar')
    shutil.move(old_pack_root, package_root)
    for root, dirs, files in os.walk(project_root):
        dirs[:] = [d for d in dirs if d not in ['.git']]
        for f in files:
            if f.startswith('foobar'):
                old = f
                f = re.sub('foobar', package, f)
                os.rename(os.path.join(root, old), os.path.join(root, f))
            t = ''
            with open(os.path.join(root, f), 'r') as g:
                t = g.read()
            with open(os.path.join(root, f), 'w') as g:
                g.write(re.sub('foobar', package, t))


def fixup_extras(project, package, github):
    pass
