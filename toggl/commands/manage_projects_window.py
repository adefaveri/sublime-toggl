import sublime

from .base_manage_window import BaseManageWindowCommand
from ..utils.palette import show_palette
from ..utils.cache import Cache

class ManageProjectsCommand(BaseManageWindowCommand):
    def run(self):
        self.workspaces = self.retrieve_workspaces()

        show_palette(self.window, ['Workspace: ' + workspace['name'] for workspace in self.workspaces], self.chosen_workspace)

    def chosen_workspace(self, workspace_pick):
        if workspace_pick is -1:
            return

        self.projects = self.retrieve_projects(self.workspaces[workspace_pick]['id'])

        show_palette(self.window, ['Create new project'] + [project['name'] for project in self.projects], lambda project_pick: self.chosen_project(project_pick, self.workspaces[workspace_pick]['id']))

    def chosen_project(self, project_pick, workspace_pick):
        if project_pick is -1:
            return

        if project_pick is 0:
            self.window.show_input_panel('New project\'s name:', '', lambda project_name: self.create_new_project(workspace_pick, project_name), None, None)
            return

        project_id = self.projects[project_pick - 1]['id']
        show_palette(self.window, ['Rename'], lambda action: self.chosen_project_action(action, project_id))

    def create_new_project(self, workspace_pick, project_name):
        project = self.project_api.create({'workspace_id': workspace_pick, 'name': project_name})

        if not project:
            sublime.error_message('Error creating project.')
        else:
            sublime.status_message('Project ' + project_name + ' created.')
            Cache.store('projects', Cache.retrieve('projects') + [project])

    def chosen_project_action(self, project_action, project_id):
        if project_action is -1:
            return

        if project_action is 0:
            self.window.show_input_panel('New name:', '', lambda new_project_name: self.update_project_name(new_project_name, project_id), None, None)

    def update_project_name(self, new_project_name, project_id):
        updated_project = self.project_api.update(project_id, {'name': new_project_name})

        if not updated_project:
            sublime.error_message('Error renaming project.')
        else:
            sublime.status_message('Project renamed to ' + new_project_name)
            projects = Cache.retrieve('projects')
            for key, project in enumerate(projects):
                if project['id'] == updated_project['id']:
                    projects[key] = updated_project
                    break
            Cache.store('projects', projects)
