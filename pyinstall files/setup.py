from distutils.core import setup
import sys
if len(sys.argv) == 1:
    sys.argv.append("pyinstaller docfillv2")
setup(options = {"py2exe": {"includes": ["tkinter", "openfiles", "os"]}}, console=['DocFillv2.py'])
#setup(console=['openfiles.py'])
