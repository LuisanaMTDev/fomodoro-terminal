"""Utilities."""
from enum import Enum
from time import sleep
from os.path import dirname, abspath, join


class States(Enum):
    """States of the stopwatch and the timer."""
    WITHOUT_START: str = 'Without start'
    START: str = 'Start'
    PAUSE: str = 'Pause'
    STOP: str = 'Stop'

SECONDS_FORMAT = '%M:%S'

INFO_FILE = join(dirname(abspath(__file__)), 'info.json')

#def calculate_amount_of_seconds_for_the_timer(stopwatch: Stopwatch):
#    """To calculate the amount of seconds for the timer."""
#    amount_of_seconds_for_the_timer: int = (stopwatch.elapsed_seconds / 5) * 60
#
#    return amount_of_seconds_for_the_timer


#def decrease(break_time_in_seconds: int, timer: Timer):
#    """To decrease amount of break time seconds."""
#    timer.break_time_in_seconds = break_time_in_seconds
#
#    while timer.state == States.START or timer.state == States.RESTART:
#        sleep(1.0)
#        timer.break_time_in_seconds -= 1
