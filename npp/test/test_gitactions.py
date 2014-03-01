import unittest
from unittest.mock import Mock, patch
from subprocess import CalledProcessError

from npp.gitactions import get_git_username, get_git_email, add_repo_remote, set_repo_remote
from npp.gitactions import git_pull_from_remote, git_fetch_from_remote
from npp.gitactions import git_merge_from_remote, init_git_repo


class TestGetGitEmail(unittest.TestCase):
    @patch('subprocess.check_call', Mock(side_effect=CalledProcessError('', '')))
    def test__get_git_email__no_email(self):
        self.assertEqual(get_git_email(), '')

    @patch('subprocess.check_call', Mock(return_value='jeff@email.com'))
    def test__get_git_email__valid_email(self):
        self.assertEqual(get_git_email(), 'jeff@email.com')

    @unittest.skip('Need to add email address validation')
    @patch('subprocess.check_call', Mock(return_value='this is not an email'))
    def test__get_git_email__invalid_email(self):
        self.assertEqual(get_git_email(), '')


class TestGetGitUsername(unittest.TestCase):
    @patch('subprocess.check_call', Mock(side_effect=CalledProcessError('', '')))
    def test__get_git_username__no_username(self):
        self.assertEqual(get_git_username(), '')

    @patch('subprocess.check_call', Mock(return_value='Jeff Kloosterman'))
    def test__get_git_username__valid_username(self):
        self.assertEqual(get_git_username(), 'Jeff Kloosterman')


class TestInitGitRepo(unittest.TestCase):
    @patch('subprocess.check_call', Mock(return_value='Initialized empty Git repository in /path/to/git/NewPyProj/.git/'))
    def test__init_git_repo__success(self):
        self.assertTrue(init_git_repo())

    @patch('subprocess.check_call', Mock(side_effect=CalledProcessError('', '')))
    def test__init_git_repo__failure(self):
        self.assertFalse(init_git_repo())


class TestAddRepoRemote(unittest.TestCase):
    @patch('subprocess.check_call', Mock(return_value='some message about remote added'))
    def test__add_repo_remote__success(self):
        self.assertTrue(add_repo_remote('testing', 'https://testurl.com/repo.git'))

    @patch('subprocess.check_call', Mock(side_effect=CalledProcessError('', '')))
    def test__add_repo_remote__failure(self):
        self.assertFalse(add_repo_remote('testing', 'https://testurl.com/repo.git'))


class TestSetRepoRemote(unittest.TestCase):
    @patch('subprocess.check_call', Mock(return_value='some message about remote added'))
    def test__set_repo_remote__success(self):
        self.assertTrue(set_repo_remote('testing', 'https://testurl.com/repo.git'))

    @patch('subprocess.check_call', Mock(side_effect=CalledProcessError('', '')))
    def test__set_repo_remote__failure(self):
        self.assertFalse(set_repo_remote('testing', 'https://testurl.com/repo.git'))


class TestGitPullFromRemote(unittest.TestCase):
    @patch('npp.gitactions.git_fetch_from_remote', Mock(return_value=True))
    @patch('npp.gitactions.git_merge_from_remote', Mock(return_value=True))
    @patch('subprocess.check_call', Mock(return_value='some message about remote added'))    
    def test__git_pull_from_remote__success(self):
        self.assertTrue(git_pull_from_remote('testing', 'https://testurl.com/repo.git'))

    @patch('npp.gitactions.git_fetch_from_remote', Mock(return_value=False))
    @patch('subprocess.check_call', Mock(return_value='some message about remote added'))
    def test__git_pull_from_remote__failure_fetch(self):
        self.assertFalse(git_pull_from_remote('testing', 'https://testurl.com/repo.git'))

    @patch('npp.gitactions.git_merge_from_remote', Mock(return_value=False))
    @patch('subprocess.check_call', Mock(return_value='some message about remote added'))
    def test__git_pull_from_remote__failure_merge(self):
        self.assertFalse(git_pull_from_remote('testing', 'https://testurl.com/repo.git'))


class TestGitFetchFromRemote(unittest.TestCase):
    @patch('subprocess.check_call', Mock(return_value='some message about remote added'))    
    def test__git_fetch_from_remote__success(self):
        self.assertTrue(git_fetch_from_remote('testing'))

    @patch('subprocess.check_call', Mock(side_effect=CalledProcessError('', '')))
    def test__git_fetch_from_remote__failure_merge(self):
        self.assertFalse(git_fetch_from_remote('testing'))


class TestGitMergeFromRemote(unittest.TestCase):
    @patch('subprocess.check_call', Mock(return_value='some message about remote added'))    
    def test__git_merge_from_remote__success(self):
        self.assertTrue(git_merge_from_remote('testing', 'https://testurl.com/repo.git'))

    @patch('subprocess.check_call', Mock(side_effect=CalledProcessError('', '')))
    def test__git_merge_from_remote__failure_merge(self):
        self.assertFalse(git_merge_from_remote('testing', 'https://testurl.com/repo.git'))

