import sys

sys.path.extend(['/'.join(__file__.split('/')[:-1]),
                 '/usr/local/lib/python3/dist-packages/',
                 '/usr/lib/python3/dist-packages/'])
from app import app as application
