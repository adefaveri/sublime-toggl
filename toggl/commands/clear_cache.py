import sublime
import sublime_plugin

from ..utils.cache import Cache

class ClearCacheCommand(sublime_plugin.WindowCommand):
    def run(self):
        Cache.delete('workspaces')
        Cache.delete('projects')

        sublime.status_message('Cache cleared!')