import os
import sys

# py -m venv
# @see: https://modwsgi.readthedocs.io/en/develop/user-guides/virtual-environments.html
# @see: https://stackoverflow.com/questions/25020451/no-activate-this-py-file-in-venv-pyvenv
activate_this = os.path.join(os.environ['PYTHON_HOME'], 'myapps/flask', 'yankue', 'venv/Scripts/activate_this.py')
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))

BASE_DIR = os.path.join(os.path.dirname(__file__))
if BASE_DIR not in sys.path:
    sys.path.append(BASE_DIR)

from yankue import create_app
application = create_app()
