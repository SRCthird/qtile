#!/bin/bash

# Apply wallpaper using wal
source ~/.config/qtile/Wallpaper/setWallpaper &

# Start picom
picom --config ~/.config/picom/picom.conf &

# Start dock
python ~/.config/qtile/autostart.py & 
