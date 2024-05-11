import pytest

from fomodoro.utils import States
from fomodoro.stopwatch import prepare_stopwatch


def test_prepare_stopwatch():
    stopwatch_obj = prepare_stopwatch()

    assert stopwatch_obj.state == States.START
