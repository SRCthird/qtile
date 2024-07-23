# =========================================================
# Imports
# =========================================================
import subprocess
import os
from libqtile import hook

# =========================================================
# Configuration Imports
# =========================================================
from keys import keys, mod, terminal
from groups import groups
from layouts import layouts
from screens import widget_defaults, extension_defaults, screens
from mouse import mouse
from floating_layout import floating_layout

# =========================================================
# Other Configurations
# =========================================================
dgroups_key_binder = None
dgroups_app_rules = []
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = True
wl_input_rules = None
wmname = "LG3D"

# =========================================================
# Autostart
# =========================================================
@hook.subscribe.startup_once
def autostart():
    subprocess.call([os.path.expanduser('.config/qtile/autostart_once.sh')])
