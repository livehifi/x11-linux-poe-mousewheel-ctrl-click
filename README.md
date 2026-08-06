# x11-linux-poe-mousewheel-ctrl-click
Quick python program that helps you transfer items in Path of Exile more efficiently via ctrl mousewheel as click input. Follows the PoE one action rule per ToS. Only for clicking the items with a wheel instead of a mouse.

Pre req is python3 and pyinput
```python3 -m pip install --user pynput```

Just 
```chmod +x```
and
```./poelmbroll.py```

Bazzite specific icon on desktop
```cat << 'EOF' > ~/Desktop/poelmbroll.desktop
[Desktop Entry]
Type=Application
Name=Poe Lmbroll
Comment=Launch Poe Lmbroll Script
Exec=python3 /path/to/poelmbroll.py
Icon=utilities-terminal
Terminal=true
Categories=Utility;
EOF
chmod +x ~/Desktop/poelmbroll.desktop
```

Example
[example.webm](https://github.com/user-attachments/assets/d5b1d55b-80e8-4f88-a2e6-aa40a762873f)
