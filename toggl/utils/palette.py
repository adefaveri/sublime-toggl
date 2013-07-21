import sublime

def show_palette(window, options, done_callback):
    sublime.set_timeout(lambda: window.show_quick_panel(options, done_callback), 10)