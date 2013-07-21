from .toggl_base_api import TogglBaseApi

class TogglTimeEntryApi(TogglBaseApi):
    TIME_ENTRY_START_URL = 'https://www.toggl.com/api/v8/time_entries/start'
    TIME_ENTRY_STOP_URL  = 'https://www.toggl.com/api/v8/time_entries/%s/stop'

    def start(self, project_id, description):
        return self.get_response(self.request(self.TIME_ENTRY_START_URL, self.prepare_datas({'time_entry': {'description': description, 'pid': project_id}}), {'Content-type': 'application/json'}, 'POST'))['data']

    def stop(self, time_entry_id):
        return self.get_response(self.request(self.TIME_ENTRY_STOP_URL % (time_entry_id), None, {'Content-type': 'application/json'}, 'PUT'))['data']
