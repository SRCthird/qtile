import subprocess
import time
import os

while True:
    try:
        # CSS file location.
        os.chdir(os.path.expanduser('~/.config/qtile'))

        # Apps to display in dock.
        search_apps = ["wezterm", "firefox", "spotify", "discord"]

        command = [
            "python3",
            "-m", "qtile_dock.cli",
            "launch",
            "--apps"] + search_apps + [
            "--config", os.path.expanduser('~/.config/qtile/styles.css')
        ]
        subprocess.run(command, check=True)
    except:
        print("Restarting script...")
        time.sleep(1)
