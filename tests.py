import os
import unittest


class VersionTestCases(unittest.TestCase):

    def test_tensorflow_version(self):
        import tensorflow as tf
        self.assertEqual(tf.__version__, os.environ['TENSORFLOW_VERSION'])

    def test_python_version(self):
        import sys
        self.assertEqual('{}.{}'.format(*sys.version_info[:2]),
                         os.environ['PYTHON_VERSION'])


if __name__ == '__main__':
    unittest.main()
