from pathlib import Path
import os

homeFolder = Path('/home/santi')
subfolder = Path('spam')

homeFolder / subfolder # joins paths

Path.cwd() # prints current working dir
os.getcwd # older way to get current working dir

os.chdir('/home/santi') # changes dir

os.makedirs('./esto/son/carpetas/rusas') # creates folders

Path(r'/home/santi/alba').mkdir() # create alba folder under santi (only one folder at a time)

os.path.abspath(path) # converting a relative path into absolut 