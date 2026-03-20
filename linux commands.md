# Linux Commands

## update the OS
sudo apt update && sudo apt upgrade

## install GUI in linux distro
sudo apt install lightdm
// select lightdm or or gdm3..


## start the lightdm
--------------------------
sudo service lightdm start

_see what display manager is configured_
-----------------------------------------------------------
cat /etc/X11/default-display-manager

_check OS version_
-----------------------------------
cat /etc/OS-release

_stop lightdm_
----------------------------------
sudo service lightdm stop

Install GNOME: sudo apt install ubuntu-desktop.
Install X Server: sudo apt install xserver-xorg.
Install xrdp: sudo apt install xrdp.
Connect via RDP: Use the Windows Remote Desktop Connection to connect to the [WSL instance](https://www.youtube.com/watch?v=EBRxSYv0ojg#:~:text=In%20this%20tutorial%2C%20we%20explain,to%20the%20Linux%20Desktop%20Environment.) 


MS docs: [Install commands for apps](https://learn.microsoft.com/en-us/windows/wsl/tutorials/gui-apps)


##Use Ubuntu desktop
sudo apt install ubuntu-desktop


sudo service start slim or gdm3 or lightdm


