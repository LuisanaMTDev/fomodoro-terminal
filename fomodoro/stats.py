"""This module has all code related to stats feature."""
from datetime import datetime
from sqlite3 import connect, OperationalError, Cursor, Connection
import click as ck

from fomodoro.utils import DATA_BASE_FILE

# IDEA FOR TEST: Print whatever raised exception on code that use sqlite3.
def create_table(cursor: Cursor, connection: Connection, table_name: str) -> None:
    """This function create stopwatch and timer tables on fomodoro_terminal database."""
    try:
        cursor.execute(
            f"""
            CREATE TABLE {table_name}(
            id INTEGER NOT NULL,
            seconds INTEGER NOT NULL,
            date TEXT NOT NULL,
            PRIMARY KEY(id AUTOINCREMENT)
            );
            """
        )
        connection.commit()
    except OperationalError:
        pass


def add_stopwatch_record(elapsed_seconds: int) -> None:
    """This function create a new record on stopwatch table."""
    date = datetime.now().isoformat()[0:10]

    connection = connect(DATA_BASE_FILE)
    cursor = connection.cursor()

    create_table(cursor, connection, "stopwatch")

    #IDEA FOR TEST: After execute this function execute a select query
    #to compare result data with insert insert data.
    cursor.execute(
        """
        INSERT INTO stopwatch(seconds, date) VALUES (?, ?)
        """,
        (elapsed_seconds, date)
    )
    connection.commit()

    connection.close()


def add_timer_record(amount_of_seconds_for_the_timer: int) -> None:
    """This function create a new record on timer table."""
    date = datetime.now().isoformat()[0:10]

    connection = connect(DATA_BASE_FILE)
    cursor = connection.cursor()

    create_table(cursor, connection, "timer")

    #IDEA FOR TEST: After execute this function execute a select query
    #to compare result data with insert insert data.
    cursor.execute(
        """
        INSERT INTO timer(seconds, date) VALUES (?, ?)
        """,
        (amount_of_seconds_for_the_timer, date)
    )
    connection.commit()

    connection.close()


def get_stats() -> None:
    """This function get stopwatch and timer stats."""


@ck.command
def show_stats():
    """This command show stopwatch and timer stats for user."""
    ck.echo("Hello world!")
