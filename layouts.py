from libqtile import layout
from schema import schema

layouts = [
    layout.Columns(
        margin=10, border_focus=schema['layout_border'],
        border_normal=schema['layout_border'],
        border_width=0
    ),
    layout.Max(
        border_focus=schema['layout_border'],
        border_normal=schema['layout_border'],
        margin=10,
        border_width=0,
    ),
    layout.Floating(
        border_focus=schema['layout_border'],
        border_normal=schema['layout_border'],
        margin=10,
        border_width=0,
    ),
    layout.Matrix(
        border_focus=schema['layout_border'],
        border_normal=schema['layout_border'],
        margin=10,
        border_width=0,
    ),
    layout.MonadTall(
        border_focus=schema['layout_border'],
        border_normal=schema['layout_border'],
        margin=4,
        border_width=0,
    ),
    layout.MonadWide(
        border_focus=schema['layout_border'],
        border_normal=schema['layout_border'],
        margin=10,
        border_width=0,
    ),
    layout.Tile(
        border_focus=schema['layout_border'],
        border_normal=schema['layout_border'],
    ),
    #  layout.Stack(num_stacks=2),
    #  layout.Bsp(),
    #  layout.RatioTile(),
    #  layout.TreeTab(),
    #  layout.VerticalTile(),
    #  layout.Zoomy(),
]
