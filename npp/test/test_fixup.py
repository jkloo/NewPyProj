import unittest
from unittest.mock import Mock, patch
from subprocess import CalledProcessError

from npp.fixup import fixup_project, fixup_package, fixup_extras
