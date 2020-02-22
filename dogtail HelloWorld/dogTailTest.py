
import os
import shutil
import tempfile
import time
import signal

from dogtail.procedural import *

os.environ["LC_ALL"] = "C"

dirname = tempfile.mkdtemp()
filename = os.path.join(dirname, "hello.txt")
string = "Hello world!"

pid = run("gedit")
focus.application("gedit")
type(string)

keyCombo("<ctrl>s")
type(filename)
focus.widget("Save As")
click.button("Save")

os.kill(pid,signal.SIGSTOP) ##dogtail isn't detecting the close button...
                            ##So I'm basically I'm working around it
                            ##Using a GUI inspector(Accerciser) it refuses
                            ##to accept the 'x' as an option. Maybe something
                            ##I'm over looking.

f = open(filename,"r")
saved_string = f.read()
if saved_string != string + "\n": 
    print ("error: bad content saved")
    print (repr(saved_string))
else:
    print ("ok")
