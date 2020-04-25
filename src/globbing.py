#!/usr/bin/env python3
from glob import glob

ignore = [
    "widget.c",
    "ftcrfont.c",
    "gfilenotify.c",
    "json.c",
    "emacsgtkfixed.c",
    "kqueue.c",
    "fringe.c",
    "fontset.c",
    "image.c",
    "mini-gmp.c",
    "termcap.c",
    "tparam.c",
    "floatfn.c",
    "xftfont.c",
    "xwidget.c",
    "xmenu.c",
    "xsettings.c",
    "xfont.c",
    "xselect.c",
    "xfns.c",
    "xterm.c",
    "xrdb.c",
    "inotify.c",
    "emacs-module.c",
    "ralloc.c",
]

files = glob("*.c")
files = filter(lambda f: not "w32" in f, files)
files = filter(lambda f: not "unex" in f, files)
files = filter(lambda f: not f.startswith("ft"), files)
files = filter(lambda f: not f.startswith("hb"), files)
files = filter(lambda f: not f in ignore, files)
print("\n".join(files))
