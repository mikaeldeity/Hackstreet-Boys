# Enable Python support and load DesignScript library
import clr
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *

import sys

clr.AddReference('IronPython')
sys.path.append(r'C:\\Program Files (x86)\\IronPython 2.7\\Lib')

import os.path
import time
import subprocess

username = os.environ.get("USERNAME")
path = "C:\\Users\\{}\\AppData\\Local\\FaceMesh\\".format(username)

pyscript = path + "RunPY.bat"

objfile = path + "FaceMeshOutput\\FaceMesh.obj"

os.remove(objfile)

subprocess.call([pyscript])

while not os.path.exists(objfile):
    time.sleep(1)

# Assign your output to the OUT variable.

OUT = objfile