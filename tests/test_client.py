import unittest

from client import client_options


class ClientOptionsTests(unittest.TestCase):
    def test_timeout_option(self):
        self.assertEqual(client_options(), {"timeout_seconds": 30})

    def test_options_are_independent(self):
        options = client_options()
        options["timeout_seconds"] = 1
        self.assertEqual(client_options()["timeout_seconds"], 30)


if __name__ == "__main__":
    unittest.main()
