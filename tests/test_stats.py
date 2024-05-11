import pytest
from click.testing import CliRunner

from fomodoro.stats import show_stats


def test_show_stats():
    runner = CliRunner()

    result = runner.invoke(show_stats)

    assert result.exit_code == 0
