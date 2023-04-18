# [cinnamon_titlebar_fix](https://github.com/rtmigo/cinnamon_titlebar_fix)

Sets the size of buttons in **Cinnamon title** bar to 140%.

Tested in **Linux Mint 21.1**.

## Set buttons to 140%

```bash
wget -qO- https://raw.githubusercontent.com/rtmigo/cinnamon_titlebar_fix/dev/fix_titlebar.py > /tmp/fix_titlebar.py \
  && python3 /tmp/fix_titlebar.py 
```

That's all. After that, **restart Cinnamon** (Ctrl+Alt+Esc).

##  What this script does

It **overwrites** the `~/.config/gtk-3.0/gtk.css`. By default, there is no such 
file. If may exist if you already tried to manually customize Cinnamon.

## Set buttons to default 100%

If you want to restore original title bar, just run

```bash
rm ~/.config/gtk-3.0/gtk.css
```

and restart Cinnamon.

## Old gtk.css

If you had `~/.config/gtk-3.0/gtk.css` before running the script, its backup 
will be saved under name `~/.config/gtk-3.0/gtk.css/.bak{N}`.
