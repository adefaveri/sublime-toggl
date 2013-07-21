# Toggl Timer

Track your time on [Toggl](https://www.toggl.com/) from Sublime Text!

## Installation

Waiting integration in Package Control

## Usage

### Configuration

Enter you Toggl API key (found in [your profile](https://www.toggl.com/user/edit)) in Toggl Timer.sublime-preferences (Preferences > Package Settings > Toggl Timer)

### Manage projects (add/rename)

Open the Command Palette then search "Toggl Timer: Manage Workspaces' Projects"

### Start/end a time entry

Open the Command Palette then search "Toggl Timer: Time Entries"

### Clearing the cache

To avoid being too long and exchange too much with the API, this package uses a cache system. To clear it (i.e. if you added a workspace/project from other Toggl client), open Command Palette and search "Toggl Timer: Clear Cache"

## FAQ

* __I can't create workspace, delete workspace nor delete project from this package.__

I know that, and I can't. Unfortunatly the Toggl API doesn't allow to do so.

* __The first time the package loads the workspaces/projects list, it's a bit long.__

It's because it's loading the lists from the API, so it mainly depends on your brandwidth. But once it's loaded a first time, there is little cache system to avoid waiting too much after that.