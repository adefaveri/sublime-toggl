import unittest

from toggl.utils.toggl_api.toggl_workspace_api import TogglWorkspaceApi

API_TOKEN = input("\nYour Toggl api token:\n")

class TogglWorkspaceApiTest(unittest.TestCase):
    def setUp(self):
        self.toggl_workspace = TogglWorkspaceApi()
        self.toggl_workspace.authenticate(API_TOKEN)

    def test_get_workspaces_list(self):
        self.assertIsInstance(self.toggl_workspace.get_workspaces(), list)

if __name__ == '__main__':
    unittest.main()