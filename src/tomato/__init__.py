import sys

sys.path += sys.modules["tomato"].__path__

from .main import run_daemon
