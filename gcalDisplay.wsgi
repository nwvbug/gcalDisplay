#!/usr/bin/python
import sys
import os



sys.path.append('/usr/local/var/www/gcalDisplay/venv/lib/python3.10/site-packages')

os.chdir("/usr/local/var/www/gcalDisplay/server)

from server.flask_app import app as application