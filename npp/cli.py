#!/usr/bin/env python

""" Command line interface for the NewPyProj tool. """

import os
import argparse

from npp import TEMPLATE_URL
from npp.fixup import fixup_project, fixup_package, fixup_extras
from npp.gitactions import init_git_repo, add_repo_remote, git_pull_from_remote, set_repo_remote


def _generate_args(args):
    """ Parse the passed in args and return the corresponding namespace. """
    parser = argparse.ArgumentParser()
    parser.add_argument('project', help='The name of the new project you want to start.')
    parser.add_argument('package', help='The name of the package you are developing.')
    parser.add_argument('--github', help='The github account you want to create this project on.', default='')
    return parser.parse_args(args)


def main(args=None):
    """ The entry point for the npp tool. """
    args = _generate_args(args)
    os.mkdir(args.project)
    tmp = os.getcwd()
    os.chdir(args.project)
    init_git_repo()
    if args.github:
        template_url = 'https://github.com/{}/template-python.git'.format(args.github)
        add_repo_remote('template', template_url)
        if not git_pull_from_remote('template'):
            set_repo_remote('template', TEMPLATE_URL)
            git_pull_from_remote('template')
    else:
        add_repo_remote('template', TEMPLATE_URL)
        git_pull_from_remote('template')

    os.chdir(tmp)
    fixup_project(args.project)
    fixup_package(args.project, args.package)
    fixup_extras(args.project, args.package, args.github)


if __name__ == '__main__':  # pragma: no cover
    main()
