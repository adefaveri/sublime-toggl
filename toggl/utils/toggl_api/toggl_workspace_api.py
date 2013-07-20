from .toggl_base_api import TogglBaseApi

class TogglWorkspaceApi(TogglBaseApi):
    WORKSPACES_LIST_URL        = 'https://www.toggl.com/api/v8/workspaces'

    def get_workspaces(self):
        return self.get_response(self.request(self.WORKSPACES_LIST_URL))
