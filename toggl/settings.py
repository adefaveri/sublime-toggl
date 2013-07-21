import sublime

def get_user_api_token():
    api_token = sublime.load_settings(get_preferences_filename()).get('api_token')

    if not api_token:
        sublime.error_message('No API Token found, please fill your Toggl API Token in the ' + get_preferences_filename() + ' file')
        raise Exception('API Token not found')

    return api_token

def get_preferences_filename():
    return 'Toggl Timer.sublime-settings'
