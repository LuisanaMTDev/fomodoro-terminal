"""Functions of the stopwatch."""
from fomodoro.core.utils import Stopwatch, StopwatchStates, increase


def start(stopwatch: Stopwatch) -> None:
    """Start the stopwatch and increase its amount of elapsed seconds."""
    stopwatch.state = StopwatchStates.START

    increase(stopwatch)


def pause(stopwatch: Stopwatch) -> None:
    """Pause the stopwatch."""
    stopwatch.state = StopwatchStates.PAUSE


def resume(stopwatch: Stopwatch) -> None:
    """Resume the stopwatch and continue increasing its amount of elapsed seconds."""
    stopwatch.state = StopwatchStates.RESTART

    increase(stopwatch)


def stop(stopwatch: Stopwatch) -> None:
    """Stop the stopwatch."""
    stopwatch.state = StopwatchStates.STOP
