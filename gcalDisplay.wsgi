#!/usr/bin/python
import sys
import os

sys.path.insert(0,"/usr/local/var/www/gcalDisplay")
sys.path.insert(1,"/usr/local/var/www/gcalDisplay/server")

sys.path.append('/usr/local/var/www/gcalDisplay/venv/lib/python3.10/site-packages')

os.chdir("/usr/local/var/www/gcalDisplay")

from server.flask_app import app as application