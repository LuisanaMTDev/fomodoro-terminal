"""Functions of the stopwatch."""
from fomodoro.utils import Stopwatch, States, increase


def start(stopwatch: Stopwatch) -> None:
    """Start the stopwatch and increase its amount of elapsed seconds."""
    stopwatch.state = States.START

    increase(stopwatch)


def pause(stopwatch: Stopwatch) -> None:
    """Pause the stopwatch."""
    stopwatch.state = States.PAUSE


def resume(stopwatch: Stopwatch) -> None:
    """Resume the stopwatch and continue increasing its amount of elapsed seconds."""
    stopwatch.state = States.RESTART

    increase(stopwatch)


def stop(stopwatch: Stopwatch) -> None:
    """Stop the stopwatch."""
    stopwatch.state = States.STOP
