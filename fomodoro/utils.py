"""Utilities."""
from enum import Enum
from time import sleep


class States(Enum):
    """States of the stopwatch and the timer."""
    WITHOUT_START: bool = True
    START: bool = True
    PAUSE: bool = True
    RESTART: bool = True
    STOP: bool = True

# STOPWATCH
class Stopwatch():
    """To can manipulate the stopwatch easiest by functions."""
    def __init__(self) -> None:
        self.state = States.WITHOUT_START
        self.elapsed_seconds = 0

stopwatch_obj = Stopwatch()


def increase(stopwatch: Stopwatch) -> None:
    """To increase amount of elapsed seconds."""
    while stopwatch.state == States.START or stopwatch.state == States.RESTART:
        sleep(1.0)
        stopwatch.elapsed_seconds += 1



def calculate_amount_of_seconds_for_the_timer(stopwatch: Stopwatch):
    """To calculate the amount of seconds for the timer."""
    amount_of_seconds_for_the_timer: int = (stopwatch.elapsed_seconds / 5) * 60

    return amount_of_seconds_for_the_timer


# TIMER
class Timer():
    """To can manipulate the timer easiest by functions."""
    def __init__(self) -> None:
        self.state = States.WITHOUT_START
        self.break_time_in_seconds = 0

timer_obj = Timer()


def decrease(break_time_in_seconds: int, timer: Timer):
    """To decrease amount of break time seconds."""
    timer.break_time_in_seconds = break_time_in_seconds

    while timer.state == States.START or timer.state == States.RESTART:
        sleep(1.0)
        timer.break_time_in_seconds -= 1
