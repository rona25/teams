import os
import unittest


class BaseTestCase(unittest.TestCase):
    def setUp(self):
        super(BaseTestCase, self).setUp()

        # do some common setup stuff
        pass

    def tearDown(self):
        super(BaseTestCase, self).tearDown()

        # do some common teardown stuff
        pass

    def get_data_dir(self):
        dir = os.path.realpath(
            os.path.join(
                os.path.dirname(__file__),
                '..',
                '..',
                'data',
                'teams',
            )
        )
        return dir
