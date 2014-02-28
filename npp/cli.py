#!/usr/bin/env python

import os
import argparse

from npp.fixup import fixup_project, fixup_package, fixup_extras
from npp.fixup import _init_git_repo, _add_repo_remote, _git_pull_from_remote


TEMPLATE_URL =  'https://github.com/jacebrowning/template-python.git'


def _generate_args(args):
    parser = argparse.ArgumentParser()
    parser.add_argument('project', help='The name of the new project you want to start.')
    parser.add_argument('package', help='The name of the package you are developing.')
    parser.add_argument('--github', help='The github account you want to create this project on.')
    return parser.parse_args(args)


def main(args=None):
    args = _generate_args(args)
    os.mkdir(args.project)
    tmp = os.getcwd()
    os.chdir(args.project)
    _init_git_repo()
    _add_repo_remote('template', TEMPLATE_URL)
    _git_pull_from_remote('template')
    os.chdir(tmp)
    fixup_project(args.project)
    fixup_package(args.project, args.package)


if __name__ == '__main__':
    main()