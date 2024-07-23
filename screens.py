from libqtile import bar, widget, qtile
from libqtile.config import Screen
from schema import schema

widget_defaults = dict(
    font="sans",
    fontsize=12,
    padding=3,
)
extension_defaults = [widget_defaults.copy()]


def search():
    qtile.cmd_spawn("rofi -show drun")


def power():
    qtile.cmd_spawn("sh -c ~/.config/qtile/Scripts/power")


screens = [
    Screen(
        top=bar.Bar(
            [
                widget.Spacer(
                    length=15,
                    background=schema['background1'],
                ),
                widget.Image(
                    filename='~/.config/qtile/Assets/launch_Icon.png',
                    margin=2,
                    background=schema['background1'],
                    mouse_callbacks={"Button1": power},
                ),
                widget.Image(
                    filename='~/.config/qtile/Assets/6.png',
                ),
                widget.GroupBox(
                    fontsize=24,
                    borderwidth=3,
                    highlight_method='block',
                    active=schema['foreground1'],
                    block_highlight_text_color=schema['foreground2'],
                    highlight_color=schema['highlight'],
                    inactive=schema['background1'],
                    foreground=schema['highlight'],
                    background=schema['background2'],
                    this_current_screen_border=schema['background2'],
                    this_screen_border=schema['background2'],
                    other_current_screen_border=schema['background2'],
                    other_screen_border=schema['background2'],
                    urgent_border=schema['urgent_border'],
                    rounded=True,
                    disable_drag=True,
                ),
                widget.Spacer(
                    length=8,
                    background=schema['background2'],
                ),
                widget.Image(
                    filename='~/.config/qtile/Assets/1.png',
                ),
                widget.Image(
                    filename='~/.config/qtile/Assets/layout.png',
                    background=schema['background2']
                ),
                widget.CurrentLayout(
                    background=schema['background2'],
                    foreground=schema['foreground1'],
                    fmt='{}',
                    font="JetBrains Mono Bold",
                    fontsize=13,
                ),
                widget.Image(
                    filename='~/.config/qtile/Assets/5.png',
                ),
                widget.Image(
                    filename='~/.config/qtile/Assets/search.png',
                    margin=2,
                    background=schema['background1'],
                    mouse_callbacks={"Button1": search},
                ),
                widget.TextBox(
                    fmt='Search',
                    background=schema['background1'],
                    font="JetBrains Mono Bold",
                    fontsize=13,
                    foreground=schema['foreground1'],
                    mouse_callbacks={"Button1": search},
                ),
                widget.Image(
                    filename='~/.config/qtile/Assets/4.png',
                ),
                widget.WindowName(
                    background=schema['background2'],
                    format="{name}",
                    font="JetBrains Mono Bold",
                    fontsize=13,
                    foreground=schema['foreground1'],
                    empty_group_string='Desktop',

                ),
                widget.Image(
                    filename='~/.config/qtile/Assets/3.png',
                ),
                widget.Systray(
                    background=schema['background1'],
                    fontsize=2,
                ),
                widget.TextBox(
                    text=' ',
                    background=schema['background1'],
                ),
                widget.Image(
                    filename='~/.config/qtile/Assets/6.png',
                    background=schema['background2'],
                ),
                widget.Image(
                    filename='~/.config/qtile/Assets/Drop1.png',
                ),
                widget.Net(
                    format=' {up}   {down} ',
                    background=schema['background2'],
                    foreground=schema['foreground1'],
                    font="JetBrains Mono Bold",
                    prefix='k',
                ),
                widget.Image(
                    filename='~/.config/qtile/Assets/2.png',
                ),
                widget.Spacer(
                    length=8,
                    background=schema['background2'],
                ),
                widget.Image(
                    filename='~/.config/qtile/Assets/Misc/ram.png',
                    background=schema['background2'],
                ),
                widget.Spacer(
                    length=-7,
                    background=schema['background2'],
                ),
                widget.Memory(
                    background=schema['background2'],
                    format='{MemUsed: .0f}{mm}',
                    foreground=schema['foreground1'],
                    font="JetBrains Mono Bold",
                    fontsize=13,
                    update_interval=5,
                ),
                widget.Image(
                    filename='~/.config/qtile/Assets/Drop2.png',
                ),
                widget.Image(
                    filename='~/.config/qtile/Assets/2.png',
                ),
                widget.Spacer(
                    length=8,
                    background=schema['background2'],
                ),
                widget.BatteryIcon(
                    theme_path='~/.config/qtile/Assets/Battery/',
                    background=schema['background2'],
                    scale=1,
                ),
                widget.Battery(
                    font="JetBrains Mono Bold",
                    fontsize=13,
                    background=schema['background2'],
                    foreground=schema['foreground1'],
                    format='{percent:2.0%}',
                ),
                widget.Image(
                    filename='~/.config/qtile/Assets/2.png',
                ),
                widget.Spacer(
                    length=8,
                    background=schema['background2'],
                ),
                widget.Volume(
                    font="JetBrains Mono Bold",
                    fontsize=13,
                    theme_path='~/.config/qtile/Assets/Volume/',
                    emoji=True,
                    background=schema['background2'],
                ),
                widget.Spacer(
                    length=-5,
                    background=schema['background2'],
                ),
                widget.Volume(
                    font="JetBrains Mono Bold",
                    fontsize=13,
                    background=schema['background2'],
                    foreground=schema['foreground1'],
                ),
                widget.Image(
                    filename='~/.config/qtile/Assets/5.png',
                    background=schema['background2'],
                ),
                widget.Image(
                    filename='~/.config/qtile/Assets/Misc/clock.png',
                    background=schema['background1'],
                    margin_y=6,
                    margin_x=5,
                ),
                widget.Clock(
                    format='%I:%M %p',
                    background=schema['background1'],
                    foreground=schema['foreground1'],
                    font="JetBrains Mono Bold",
                    fontsize=13,
                ),
                widget.Spacer(
                    length=18,
                    background=schema['background1'],
                ),
            ],
            30,
            border_color=schema['screen_border'],
            border_width=[0, 0, 0, 0],
            margin=[15, 60, 6, 60],
        ),
    ),
]

