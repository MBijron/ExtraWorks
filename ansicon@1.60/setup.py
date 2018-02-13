from subprocess import call
from pyworks.io import Path

call([Path.combine(script_path, "ansicon.exe"), "-i"])
