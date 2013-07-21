import sublime

from .base_manage_window import BaseManageWindowCommand
from ..utils.toggl_api.toggl_time_entry_api import TogglTimeEntryApi
from ..utils.palette import show_palette
from ..settings import get_user_api_token
from ..utils.cache import Cache

class ManageTimeEntriesCommand(BaseManageWindowCommand):
    time_entry_api = None

    def run(self):
        if Cache.retrieve('time_entry_running') is None:
            options  = ['Start a time entry for project…']
            callback = self.chose_start_option
        else:
            options  = ['Stop running time entry']
            callback = self.stop_running_time_entry

        show_palette(self.window, options, callback)

    def stop_running_time_entry(self, picked_end_option):
        self.create_time_entry_api_client()
        self.time_entry_api.stop(Cache.retrieve('time_entry_running'))

        Cache.delete('time_entry_running')

        sublime.status_message('Time Entry stopped.')

    def chose_start_option(self, picked_start_option):
        if picked_start_option is -1:
            return

        self.projects = projects_options = []

        self.workspaces = self.retrieve_workspaces()
        for workspace in self.workspaces:
            projects = self.retrieve_projects(workspace['id'])
            projects_options = projects_options + [workspace['name'] + '::' + project['name'] for project in projects]
            self.projects = self.projects + projects

        show_palette(self.window, projects_options, self.ask_time_entry_desciption)

    def ask_time_entry_desciption(self, picked_project):
        if picked_project is -1:
            return

        self.create_time_entry_api_client()

        project = self.projects[picked_project]

        self.window.show_input_panel('Time Entry description:', '', lambda description: self.start_time_entry(project['id'], description), None, None)

    def start_time_entry(self, project_id, description):
        time_entry = self.time_entry_api.start(project_id, description)
        if not time_entry:
            sublime.error_message('Error starting your time entry')
        else:
            Cache.store('time_entry_running', time_entry['id'])
            sublime.status_message('Time Entry running!')

    def create_time_entry_api_client(self):
        if self.time_entry_api is None:
            self.time_entry_api = TogglTimeEntryApi()
            self.time_entry_api.authenticate(get_user_api_token())
