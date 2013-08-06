import sublime
import os
import imp
from zipfile import ZipFile

base_path = os.path.realpath(__file__ + '/../../..')
toggl_package_path = base_path + '/Packages/Toggl Timer/'

if not os.path.exists(toggl_package_path):
    package = ZipFile(base_path + '/Installed Packages/Toggl Timer.sublime-package')
    for archived in package.namelist():
        if archived.startswith('lib/'):
            package.extract(archived, toggl_package_path)

def load_ssl():
    try:
        import ssl
        assert ssl
    except ImportError:
        ssl = False

    if ssl is False and sublime.platform() == 'linux':
        plugin_path = os.path.dirname(toggl_package_path)
        if plugin_path in ('.', ''):
            plugin_path = os.getcwd()
        _ssl = None
        ssl_versions = ['0.9.8', '1.0.0', '10', '1.0.1']
        ssl_path = os.path.join(plugin_path, 'lib', 'linux')
        lib_path = os.path.join(plugin_path, 'lib', 'linux-%s' % sublime.arch())
        for version in ssl_versions:
            so_path = os.path.join(lib_path, 'libssl-%s' % version)
            try:
                filename, path, desc = imp.find_module('_ssl', [so_path])
                if filename is None:
                    print('Module not found at %s' % so_path)
                    continue
                _ssl = imp.load_module('_ssl', filename, path, desc)
                break
            except ImportError as e:
                print('Failed loading _ssl module %s: %s' % (so_path, str(e)))
        if _ssl:
            print('Hooray! %s is a winner!' % so_path)
            filename, path, desc = imp.find_module('ssl', [ssl_path])
            if filename is None:
                print('Couldn\'t find ssl module at %s' % ssl_path)
            else:
                try:
                    ssl = imp.load_module('ssl', filename, path, desc)
                except ImportError as e:
                    print('Failed loading ssl module at: %s' % str(e))
        else:
            print('Couldn\'t find an _ssl shared lib that\'s compatible with your version of linux. Sorry :(')