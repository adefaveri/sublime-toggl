import unittest

from toggl.utils.toggl_api.toggl_time_entry_api import TogglTimeEntryApi
from toggl.utils.toggl_api.toggl_workspace_api import TogglWorkspaceApi
from toggl.utils.toggl_api.toggl_project_api import TogglProjectApi

API_TOKEN = input("\nYour Toggl api token:\n")

toggl_workspace = TogglWorkspaceApi()
toggl_workspace.authenticate(API_TOKEN)
workspace_id = toggl_workspace.get_workspaces()[0]['id']

toggl_project = TogglProjectApi()
toggl_project.authenticate(API_TOKEN)
project_id = toggl_project.get_workspace_projects(workspace_id)[0]['id']

class TogglTimeEntryApiTest(unittest.TestCase):
    def setUp(self):
        self.toggl_timer_entry = TogglTimeEntryApi()
        self.toggl_timer_entry.authenticate(API_TOKEN)

    def test_start_time_entry(self):
        time_entry = self.toggl_timer_entry.start(project_id, 'Foo Time Entry')
        self.assertEqual(time_entry['description'], 'Foo Time Entry')
        self.assertEqual(self.toggl_timer_entry.stop(time_entry['id'])['id'], time_entry['id'])

if __name__ == '__main__':
    unittest.main()