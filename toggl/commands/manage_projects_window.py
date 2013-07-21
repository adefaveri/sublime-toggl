import sublime
import sublime_plugin

from ..utils.toggl_api.toggl_workspace_api import TogglWorkspaceApi
from ..utils.toggl_api.toggl_project_api import TogglProjectApi
from ..settings import get_user_api_token
from ..utils.palette import show_palette
from ..utils.cache import Cache

class ManageProjectsCommand(sublime_plugin.WindowCommand):
    workspace_api = None
    project_api   = None
    workspaces    = None
    projects      = None

    def run(self):
        self.create_workspace_api_client()
        self.create_project_api_client()

        if Cache.retrieve('workspaces') is None:
            Cache.store('workspaces', self.get_workspaces())

        self.workspaces = Cache.retrieve('workspaces')

        show_palette(self.window, ['Workspace: ' + workspace['name'] for workspace in self.workspaces], self.chosen_workspace)

    def create_workspace_api_client(self):
        if Cache.retrieve('workspace_api') is None:
            workspace_api = TogglWorkspaceApi()
            workspace_api.authenticate(get_user_api_token())
            Cache.store('workspace_api', workspace_api)

        self.workspace_api = Cache.retrieve('workspace_api')

    def create_project_api_client(self):
        if Cache.retrieve('project_api') is None:
            project_api = TogglProjectApi()
            project_api.authenticate(get_user_api_token())
            Cache.store('project_api', project_api)

        self.project_api = Cache.retrieve('project_api')

    def get_workspaces(self):
        workspaces = self.workspace_api.get_workspaces()
        return workspaces

    def chosen_workspace(self, workspace_pick):
        if workspace_pick is -1:
            return

        if Cache.retrieve('projects') is None:
            Cache.store('projects', self.project_api.get_workspace_projects(self.workspaces[workspace_pick]['id']))

        self.projects = Cache.retrieve('projects')

        show_palette(self.window, ['Create new project'] + [project['name'] for project in self.projects], lambda project_pick: self.chosen_project(project_pick, self.workspaces[workspace_pick]['id']))

    def chosen_project(self, project_pick, workspace_pick):
        if project_pick is -1:
            return

        if project_pick is 0:
            self.window.show_input_panel('New project\'s name:', '', lambda project_name: self.create_new_project(workspace_pick, project_name), None, None)

        project_id = self.projects[project_pick - 1]['id']
        show_palette(self.window, ['Rename'], lambda action: self.chosen_project_action(action, project_id))

    def create_new_project(self, workspace_pick, project_name):
        project = self.project_api.create({'workspace_id': workspace_pick, 'name': project_name})

        if not project:
            sublime.error_message('Error creating project.')
        else:
            sublime.status_message('Project ' + project_name + ' created.')

    def chosen_project_action(self, project_action, project_id):
        if project_action is -1:
            return

        if project_action is 0:
            self.window.show_input_panel('New name:', '', lambda new_project_name: self.update_project_name(new_project_name, project_id), None, None)

    def update_project_name(self, new_project_name, project_id):
        project = self.project_api.update(project_id, {'name': new_project_name})

        if not project:
            sublime.error_message('Error renaming project.')
        else:
            sublime.status_message('Project renamed to ' + new_project_name)
