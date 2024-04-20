"""Functions of the timer."""
from fomodoro.core.utils import Timer, Stopwatch, States, calculate_amount_of_seconds_for_the_timer, decrease


def start(timer: Timer, stopwatch: Stopwatch):
    """Start the timer and decrease its amount of break time seconds."""
    timer.state = States.START

    break_time_in_seconds = calculate_amount_of_seconds_for_the_timer(stopwatch)

    decrease(break_time_in_seconds, timer)


def pause(timer: Timer):
    """Pause the timer."""
    timer.state = States.PAUSE


def resume(timer: Timer):
    """Resume the timer and continue decreasing its amount of break time seconds."""
    timer.state = States.RESTART

    decrease(timer.break_time_in_seconds, timer)


def stop(timer: Timer):
    """Stop the timer."""
    timer.state = States.STOP
