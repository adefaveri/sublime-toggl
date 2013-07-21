import sublime_plugin

from ..utils.toggl_api.toggl_workspace_api import TogglWorkspaceApi
from ..utils.toggl_api.toggl_project_api import TogglProjectApi
from ..settings import get_user_api_token
from ..utils.cache import Cache

class BaseManageWindowCommand(sublime_plugin.WindowCommand):
    workspace_api = None
    project_api   = None
    workspaces    = None
    projects      = None

    def retrieve_workspaces(self):
        if Cache.retrieve('workspaces') is None:
            self.create_workspace_api_client()
            Cache.store('workspaces', self.workspace_api.get_workspaces())

        return Cache.retrieve('workspaces')

    def create_workspace_api_client(self):
        if self.workspace_api is None:
            self.workspace_api = TogglWorkspaceApi()
            self.workspace_api.authenticate(get_user_api_token())

    def retrieve_projects(self, workspace_id):
        if Cache.retrieve('projects') is None:
            self.create_project_api_client()
            Cache.store('projects', self.project_api.get_workspace_projects(workspace_id))

        return Cache.retrieve('projects')

    def create_project_api_client(self):
        if self.project_api is None:
            self.project_api = TogglProjectApi()
            self.project_api.authenticate(get_user_api_token())
