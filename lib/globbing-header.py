#!/usr/bin/env python3
from glob import glob

files = glob("*.h")
print("\n".join(files))
