import unittest

from toggl.utils.toggl_api.toggl_base_api import TogglBaseApi

API_TOKEN = input("\nYour Toggl api token:\n")

class TogglApiTest(unittest.TestCase):
    def setUp(self):
        self.toggl = TogglBaseApi()

    def test_authenticate(self):
        self.toggl.authenticate(API_TOKEN)
        self.assertTrue(self.toggl.is_logged())

if __name__ == '__main__':
    unittest.main()