#!/usr/bin/env python3
from glob import glob

ignore = [
    "fsync.c",
    "c-ctype.c",
    "readlinkat.c",
    "symlink.c",
    "gettimeofday.c",
    "regex_internal.c",
    "regexec.c",
    "regex.c",
    "regcomp.c",
    "at-func.c",
    "strtoimax.c",
    "getopt.c",
    "fstatat.c",
    "getdtablesize.c",
    "acl_entries.c",
    "xrdb.c",
    "emacs-module.c",
    "mktime.c",
    "timegm.c",
    "open.c",
    "fpending.c",
    "getopt1.c",
    "strtol.c",
]

files = glob("*.c")
files = filter(lambda f: not f in ignore, files)
print("\n".join(files))
