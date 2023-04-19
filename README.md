# [cinnamon_titlebar_fix](https://github.com/rtmigo/cinnamon_titlebar_fix)

Tweak for **Cinnamon Desktop**. Tested in **Linux Mint 21.1**. 

A one-line command that makes title bar bigger. 

Namely, "minimize", "maximize", "close" buttons will be enlarged to 140%. 
It makes the title bar more suitable for HiDPI screens.

## Set buttons to 140%

In Terminal run:

```bash
wget -qO- https://raw.githubusercontent.com/rtmigo/cinnamon_titlebar_fix/master/fix_titlebar.py > "/tmp/${USER}_fix_titlebar.py" \
  && python3 /tmp/${USER}_fix_titlebar.py  
```

That's all. After that, **restart Cinnamon** (Ctrl+Alt+Esc).

## Set buttons to default 100%

If you want to restore original title bar, just run

```bash
rm ~/.config/gtk-3.0/gtk.css
```

and restart Cinnamon.

##  What this script does

It **overwrites** the `~/.config/gtk-3.0/gtk.css`. By default, there is no such 
file. If may exist if you already tried to manually customize Cinnamon.

## Old gtk.css

If you had `~/.config/gtk-3.0/gtk.css` before running the script, its backup 
will be saved next to original file in the directory `~/.config/gtk-3.0/`.
