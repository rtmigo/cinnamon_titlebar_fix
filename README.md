# [cinnamon_titlebar_fix](https://github.com/rtmigo/cinnamon_titlebar_fix)

Tweak for **Cinnamon Desktop**. Tested in **Linux Mint 21.1**.

A one-line command that makes title bar bigger.

Namely, "minimize", "maximize", "close" buttons will be enlarged to 140%.
It makes the title bar more suitable for HiDPI screens.

This makes the interface more harmonious if you enlarge the fonts with the Font
Selection utility as well.

## Set buttons to 140%

In Terminal run:

```bash
python3 <(wget -qO- https://raw.githubusercontent.com/rtmigo/cinnamon_titlebar_fix/master/fix_titlebar.py)
```

That's all. After that, **restart Cinnamon** (Ctrl+Alt+Esc).

## Set buttons to default 100%

If you want to restore original title bar, just run

```bash
rm ~/.config/gtk-3.0/gtk.css
```

and restart Cinnamon.

## What this script does

It **overwrites** the `~/.config/gtk-3.0/gtk.css`. By default, there is no such
file. If may exist if you already tried to manually customize Cinnamon.

## Old gtk.css

If you had `~/.config/gtk-3.0/gtk.css` before running the script, its backup
will be saved next to original file in the directory `~/.config/gtk-3.0/`.

## Why 140%

Enlarging the buttons makes the icons slightly blurry. There may also be issues
with alignment.

At the moment, it was 140% that seemed to me the best compromise.

In addition, the interface magnification of 1.4 is ideal for the popular
combination of 15.6" screen with 1920x1080 resolution. A 1.4x magnification
makes the interface size equal to 101 PPI density.