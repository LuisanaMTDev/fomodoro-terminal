"""Utilities."""
from enum import Enum
from time import sleep


# STOPWATCH
class StopwatchStates(Enum):
    """States of the stopwatch."""
    WITHOUT_START: bool = True
    START: bool = True
    PAUSE: bool = True
    RESTART: bool = True
    STOP: bool = True


class Stopwatch():
    """To can manipulate the stopwatch easiest by functions."""
    def __init__(self):
        self.state = StopwatchStates.WITHOUT_START
        self.elapsed_seconds = 0

stopwatch_obj = Stopwatch()


def increase(stopwatch: Stopwatch) -> None:
    """To increase amount of elapsed seconds."""
    while stopwatch.state == StopwatchStates.START:
        sleep(1.0)
        stopwatch.elapsed_seconds += 1



def calculate_amount_of_seconds_for_the_timer(stopwatch: Stopwatch):
    """To calculate the amount of seconds for the timer."""
    amount_of_seconds_for_the_timer = stopwatch.elapsed_seconds / 5

    return amount_of_seconds_for_the_timer



# TIMER

