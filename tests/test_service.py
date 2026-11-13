import unittest

from service import outbound_timeout_seconds


class ServiceConfigTests(unittest.TestCase):
    def test_default_timeout(self):
        self.assertEqual(outbound_timeout_seconds(), 30)

    def test_timeout_is_positive(self):
        self.assertGreater(outbound_timeout_seconds(), 0)


if __name__ == "__main__":
    unittest.main()
