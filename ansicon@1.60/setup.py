from subprocess import call
from pyworks.io import Path

call([Path.combine(install_script, "ansicon.exe"), "-i"])
