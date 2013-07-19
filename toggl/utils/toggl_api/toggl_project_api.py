from toggl.utils.toggl_api.toggl_base_api import TogglBaseApi

class TogglProjectApi(TogglBaseApi):
    WORKSPACE_PROJECTS_LIST_URL  = 'https://www.toggl.com/api/v8/workspaces/%s/projects'

    def get_workspace_projects(self, workspace_id):
        return self.get_response(self.request(self.WORKSPACE_PROJECTS_LIST_URL % (workspace_id)))
