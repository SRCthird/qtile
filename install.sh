#!/bin/bash
sudo pacman -Syu  --noconfirm git

if command -v paru &>/dev/null; then
  echo "Paru $(paru -V | cut -d' ' -f2) is already installed in your system"
  paru -Syu base-devel qtile python-psutil pywal-git feh picom-jonaburg-git dunst zsh starship playerctl brightnessctl alacritty pfetch thunar rofi ranger cava pulseaudio alsa-utils neovim vim git sddm --noconfirm --needed
else
  if command -v yay &>/dev/null; then
    echo "Yay $(yay -V | cut -d' ' -f2) is installed in your system"
  else
    echo "Neither Paru nor Yay is present in your system."
    echo "Installing Yay..."
    git clone https://aur.archlinux.org/yay.git && (cd yay && makepkg -si --noconfirm)
  fi
  yay -Syu base-devel qtile python-psutil pywal-git feh picom-jonaburg-git dunst zsh starship playerctl brightnessctl alacritty pfetch thunar rofi ranger cava pulseaudio alsa-utils neovim vim git sddm --noconfirm --needed
fi 

echo "Backing up the current configs. All the backup files will be available at ~/.cozy.bak"
mkdir -p ~/.cozy.bak

for folder in .* *; do
  if [[ -d "$folder" && ! "$folder" =~ ^(\.|\.\.)$ && "$folder" != ".git" ]]; then
    if [ -d "$HOME/$folder" ]; then
      echo "Backing up ~/$folder"
      cp -r "$HOME/$folder" ~/.cozy.bak
      echo "Backed up ~/$folder successfully."
      echo "Removing old config for $folder"
      rm -rf "$HOME/$folder"
    fi
    echo "Copying new config for $folder"
    cp -r "$folder" "$HOME"
  fi
done

if pacman -Qs sddm > /dev/null; then
  echo "SDDM is already installed"
else
  echo "SDDM is not installed. Installing..."
  sudo pacman -S sddm
fi

if systemctl list-unit-files | grep enabled | grep -E 'gdm|lightdm|lxdm|lxdm-gtk3|sddm|slim|xdm'; then
  echo "Disabling currently enabled display manager"
  sudo systemctl disable --now $(systemctl list-unit-files | grep enabled | grep -E 'gdm|lightdm|lxdm|lxdm-gtk3|sddm|slim|xdm' | awk -F ' ' '{print $1}')
fi

echo "Enabling and starting SDDM"
sudo systemctl enable --now sddm

