from libqtile.config import Key
from libqtile.lazy import lazy
import qtile_dock


@lazy.function
def toggle_dock(qtile):
    qtile_dock.call("toggle")


@lazy.function
def kill_dock(qtile):
    qtile_dock.call("stop")


mod = "mod4"
terminal = "wezterm"
keys = [
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(),
        desc="Move window focus to other window"),
    Key([mod, "control"], "h", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "control"], "l", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "control"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "control"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    Key([mod, "shift"], "h", lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key([mod, "shift"], "l", lazy.layout.grow_right(),
        desc="Grow window to the right"),
    Key([mod, "shift"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "shift"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    Key([mod], "f", lazy.window.toggle_fullscreen()),
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "c", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawn("rofi -show drun"),
        desc="Spawn a command using a prompt widget"),
    Key([mod], "p", lazy.spawn(
        "sh -c ~/.config/qtile/Scripts/power"), desc='powermenu'),
    Key([mod], "t", lazy.spawn("sh -c ~/.config/qtile/Scripts/themes"),
        desc='theme_switcher'),
    Key(
        [mod],
        "o",
        lazy.function(lambda qtile: qtile_dock.call("toggle")),
        desc='Toggle dock visibility'
    ),
    Key(
        [mod, "shift"],
        "r",
        lazy.function(lambda qtile: qtile_dock.call("stop")),
        desc='Kill Qtile Dock'
    ),
    Key(
        [],
        "XF86AudioRaiseVolume",
        lazy.spawn("pactl set-sink-volume 0 +5%"),
        desc='Volume Up'
    ),
    Key(
        [],
        "XF86AudioLowerVolume",
        lazy.spawn("pactl set-sink-volume 0 -5%"),
        desc='volume down'
    ),
    Key([], "XF86AudioMute", lazy.spawn(
        "pulsemixer --toggle-mute"), desc='Volume Mute'),
    Key([], "XF86AudioPlay", lazy.spawn(
        "playerctl play-pause"), desc='playerctl'),
    Key([], "XF86AudioPrev", lazy.spawn("playerctl previous"), desc='playerctl'),
    Key([], "XF86AudioNext", lazy.spawn("playerctl next"), desc='playerctl'),
    Key([], "XF86MonBrightnessUp", lazy.spawn(
        "brightnessctl s 10%+"), desc='brightness UP'),
    Key([], "XF86MonBrightnessDown", lazy.spawn(
        "brightnessctl s 10%-"), desc='brightness Down'),
    Key([mod], "e", lazy.spawn("thunar"), desc='file manager'),
    Key([mod], "h", lazy.spawn("roficlip"), desc='clipboard'),
    Key([mod, "shift"], "s", lazy.spawn(
        "xfce4-screenshooter"), desc='Screenshot'),
]
