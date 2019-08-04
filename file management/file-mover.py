#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pathlib import Path
import shutil

source = Path('./temp')
dest = Path('./tempdest')
glob = "*.sh"

for files in source.glob(glob):
    shutil.copy(files, dest)
