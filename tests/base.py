import unittest

import pytest


@pytest.mark.usefixtures('app')
@pytest.mark.usefixtures('client_class')
class BaseTest(unittest.TestCase):
    pass
