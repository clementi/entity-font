#!/usr/bin/env fontforge
import fontforge
import sys
import os

for filename in sys.argv[1:]:
    font = fontforge.open(filename)
    basename = os.path.splitext(filename)[0]
    font.generate(basename + ".otf")
    font.generate(basename + ".ttf")
    font.close()

