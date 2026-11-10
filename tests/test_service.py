import unittest

from service import request_timeout


class ServiceConfigTests(unittest.TestCase):
    def test_default_timeout(self):
        self.assertEqual(request_timeout(), 30)

    def test_timeout_is_positive(self):
        self.assertGreater(request_timeout(), 0)


if __name__ == "__main__":
    unittest.main()
