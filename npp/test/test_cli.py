import os
import unittest
from unittest.mock import Mock, patch, ANY
from subprocess import CalledProcessError

from npp.cli import _generate_args, main


class TestGenerateArgs(unittest.TestCase):
    def test__generate_args__no_args(self):
        args = []
        self.assertRaises(SystemExit, _generate_args, args)

    def test__generate_args__positional_args(self):
        args = ['project', 'package']
        args = _generate_args(args)
        self.assertEqual(args.project, 'project')
        self.assertEqual(args.package, 'package')
        self.assertEqual(args.github, '')

    def test__generate_args__with_flags(self):
        args = ['project', 'package', '--github', 'jkloo']
        args = _generate_args(args)
        self.assertEqual(args.project, 'project')
        self.assertEqual(args.package, 'package')
        self.assertEqual(args.github, 'jkloo')


class TestMain(unittest.TestCase):
    def test__main__no_args(self):
        args = []
        self.assertRaises(SystemExit, main, args)

    @patch('os.mkdir', Mock())
    @patch('os.getcwd', Mock(return_value=os.path.basename(__file__)))
    @patch('os.chdir', Mock())
    @patch('shutil.move', Mock())
    def test__main__no_github(self):
        # patch all the things!
        with patch('npp.cli.init_git_repo', Mock(return_value=True)) as init_git_repo:
            with patch('npp.cli.add_repo_remote', Mock(return_value=True)) as add_repo_remote:
                with patch('npp.cli.git_pull_from_remote', Mock(return_value=True)) as git_pull_from_remote:
                    with patch('npp.cli.set_repo_remote', Mock(return_value=True)) as set_repo_remote:
                        with patch('npp.cli.fixup_project', Mock()) as fixup_project:
                            with patch('npp.cli.fixup_package', Mock()) as fixup_package:
                                with patch('npp.cli.fixup_extras', Mock()) as fixup_extras:
                                    args = ['project', 'package']
                                    main(args)
                                    init_git_repo.assert_called_with()
                                    add_repo_remote.assert_called_with(ANY, ANY)
                                    git_pull_from_remote.assert_called_with(ANY)
                                    self.assertFalse(set_repo_remote.called)
                                    fixup_project.assert_called_with(ANY)
                                    fixup_package.assert_called_with(ANY, ANY)
                                    fixup_extras.assert_called_with(ANY, ANY, ANY)

    @patch('os.mkdir', Mock())
    @patch('os.getcwd', Mock(return_value=os.path.basename(__file__)))
    @patch('os.chdir', Mock())
    @patch('shutil.move', Mock())
    def test__main__valid_github(self):
        # patch all the things!
        with patch('npp.cli.init_git_repo', Mock(return_value=True)) as init_git_repo:
            with patch('npp.cli.add_repo_remote', Mock(return_value=True)) as add_repo_remote:
                with patch('npp.cli.git_pull_from_remote', Mock(return_value=True)) as git_pull_from_remote:
                    with patch('npp.cli.set_repo_remote', Mock(return_value=True)) as set_repo_remote:
                        with patch('npp.cli.fixup_project', Mock()) as fixup_project:
                            with patch('npp.cli.fixup_package', Mock()) as fixup_package:
                                with patch('npp.cli.fixup_extras', Mock()) as fixup_extras:
                                    args = ['project', 'package', '--github', 'jkloo']
                                    main(args)
                                    init_git_repo.assert_called_with()
                                    add_repo_remote.assert_called_with(ANY, ANY)
                                    git_pull_from_remote.assert_called_with(ANY)
                                    self.assertFalse(set_repo_remote.called)
                                    fixup_project.assert_called_with(ANY)
                                    fixup_package.assert_called_with(ANY, ANY)
                                    fixup_extras.assert_called_with(ANY, ANY, ANY)

    @patch('os.mkdir', Mock())
    @patch('os.getcwd', Mock(return_value=os.path.basename(__file__)))
    @patch('os.chdir', Mock())
    @patch('shutil.move', Mock())
    def test__main__invalid_github(self):
        # patch all the things!
        with patch('npp.cli.init_git_repo', Mock(return_value=True)) as init_git_repo:
            with patch('npp.cli.add_repo_remote', Mock(return_value=True)) as add_repo_remote:
                with patch('npp.cli.git_pull_from_remote', Mock(return_value=False)) as git_pull_from_remote:
                    with patch('npp.cli.set_repo_remote', Mock(return_value=True)) as set_repo_remote:
                        with patch('npp.cli.fixup_project', Mock()) as fixup_project:
                            with patch('npp.cli.fixup_package', Mock()) as fixup_package:
                                with patch('npp.cli.fixup_extras', Mock()) as fixup_extras:
                                    args = ['project', 'package', '--github', 'jkloo']
                                    main(args)
                                    init_git_repo.assert_called_with()
                                    add_repo_remote.assert_called_with(ANY, ANY)
                                    git_pull_from_remote.assert_called_with(ANY)
                                    set_repo_remote.assert_called_with(ANY, ANY)
                                    fixup_project.assert_called_with(ANY)
                                    fixup_package.assert_called_with(ANY, ANY)
                                    fixup_extras.assert_called_with(ANY, ANY, ANY)
