import unittest

from toggl.utils.toggl_api.toggl_project_api import TogglProjectApi
from toggl.utils.toggl_api.toggl_workspace_api import TogglWorkspaceApi

API_TOKEN = input("\nYour Toggl api token:\n")

toggl_workspace = TogglWorkspaceApi()
toggl_workspace.authenticate(API_TOKEN)
workspace_id = toggl_workspace.get_workspaces()[0]['id']

class TogglProjectApiTest(unittest.TestCase):
    def setUp(self):
        self.toggl_project = TogglProjectApi()
        self.toggl_project.authenticate(API_TOKEN)

    def test_get_workspace_projects(self):
        self.assertIsInstance(self.toggl_project.get_workspace_projects(workspace_id), list)

    def test_create_project(self):
        self.assertEqual(self.toggl_project.create({'name': 'foo', 'workspace_id': workspace_id})['name'], 'foo')

if __name__ == '__main__':
    unittest.main()