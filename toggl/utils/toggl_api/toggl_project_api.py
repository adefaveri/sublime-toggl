from toggl.utils.toggl_api.toggl_base_api import TogglBaseApi

class TogglProjectApi(TogglBaseApi):
    WORKSPACE_PROJECTS_LIST_URL  = 'https://www.toggl.com/api/v8/workspaces/%s/projects'
    WORKSPACE_PROJECT_CREATE_URL = 'https://www.toggl.com/api/v8/projects'

    def get_workspace_projects(self, workspace_id):
        return self.get_response(self.request(self.WORKSPACE_PROJECTS_LIST_URL % (workspace_id)))

    def create(self, datas):
        return self.get_response(self.request(self.WORKSPACE_PROJECT_CREATE_URL, self.prepare_datas({'project': datas}), {'Content-type': 'application/json'}, 'POST'))['data']
