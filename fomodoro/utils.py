"""Utilities."""
from enum import Enum
from os.path import dirname, abspath, join


TIME_FORMAT = '%H:%M:%S'

INFO_FILE = join(dirname(abspath(__file__)), 'info.json')

BELL_SOUND_FILE = join(dirname(abspath(__file__)), 'bell.wav')

class States(Enum):
    """States of the stopwatch and the timer."""
    WITHOUT_START: str = ' '
    START: str = 'Start'
    PAUSE: str = 'Pause'
    STOP: str = 'Stop'