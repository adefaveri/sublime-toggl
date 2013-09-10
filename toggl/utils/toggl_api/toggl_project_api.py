from .toggl_base_api import TogglBaseApi


class TogglProjectApi(TogglBaseApi):
    WORKSPACE_PROJECTS_LIST_URL = 'https://www.toggl.com/api/v8/workspaces/%s/projects'
    WORKSPACE_PROJECT_CREATE_URL = 'https://www.toggl.com/api/v8/projects'
    WORKSPACE_PROJECT_UPDATE_URL = 'https://www.toggl.com/api/v8/projects/%s'

    def get_workspace_projects(self, workspace_id):
        return self.get_response(self.request(self.WORKSPACE_PROJECTS_LIST_URL % (workspace_id)))

    def create(self, datas):
        return self.get_response(self.request(self.WORKSPACE_PROJECT_CREATE_URL, self.prepare_datas({'project': datas}), {'Content-type': 'application/json'}, 'POST'))['data']

    def update(self, project_id, datas):
        return self.get_response(self.request(self.WORKSPACE_PROJECT_UPDATE_URL % (project_id), self.prepare_datas({'project': datas}), {'Content-type': 'application/json'}, 'PUT'))['data']
