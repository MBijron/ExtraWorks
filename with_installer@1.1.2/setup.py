from PyWorks.IO.File import File
from PyWorks.IO.Path import Path

File.write_text(Path.combine(Path.get_file_path(__file__), "generated.txt"), "This is a bunch of text created by the setup.py script")