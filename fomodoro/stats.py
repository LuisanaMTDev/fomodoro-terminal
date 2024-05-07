"""This module has all code related to stats feature."""
from datetime import datetime
from sqlite3 import connect, OperationalError, Cursor, Connection
import click as ck

from fomodoro.utils import DATA_BASE_FILE


def create_table(cursor: Cursor, connection: Connection) -> None:
    """This function create stopwatch and timer tables on fomodoro_terminal database."""
    try:
        cursor.execute(
            """
            CREATE TABLE stopwatch(
            id INTEGER NOT NULL,
            seconds INTEGER NOT NULL,
            date REAL NOT NULL,
            PRIMARY KEY(id AUTOINCREMENT)
            );
            """
        )
        connection.commit()
    except OperationalError:
        pass


def add_stopwatch_record(elapsed_seconds: int) -> None:
    """This function create a new record on stopwatch table."""
    timestamp = datetime.now().timestamp()

    connection = connect(DATA_BASE_FILE)
    cursor = connection.cursor()

    create_table(cursor, connection)

    cursor.execute(
        """
        INSERT INTO stopwatch(seconds, date) VALUES (?, ?)
        """,
        (elapsed_seconds, timestamp)
    )
    connection.commit()

    connection.close()

def add_timer_record(amount_of_seconds_for_the_timer: int) -> None:
    """This function create a new record on timer table."""
    timestamp = datetime.now().timestamp()

    connection = connect(DATA_BASE_FILE)
    cursor = connection.cursor()

    create_table(cursor, connection)

    cursor.execute(
        """
        INSERT INTO timer(seconds, date) VALUES (?, ?)
        """,
        (amount_of_seconds_for_the_timer, timestamp)
    )
    connection.commit()

    connection.close()


def get_stats() -> None:
    """This function get stopwatch and timer stats."""


@ck.command
def show_stats():
    """This command show stopwatch and timer stats for user."""
    ck.echo("Hello world!")
