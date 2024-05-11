import pytest

from fomodoro.utils import States
from fomodoro.timer import prepare_timer


def test_prepare_timer():
    timer_obj = prepare_timer()

    assert timer_obj.state == States.START
