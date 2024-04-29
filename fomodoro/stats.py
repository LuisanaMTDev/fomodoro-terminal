from datetime import datetime
from sqlite3 import connect, OperationalError
import click as ck

from fomodoro.utils import DATA_BASE_FILE


def add_stopwatch_record(elapsed_seconds: int):
    timestamp = datetime.now().timestamp()

    connection = connect(DATA_BASE_FILE)
    cursor = connection.cursor()

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

    cursor.execute(
        """
        INSERT INTO stopwatch(seconds, date) VALUES (?, ?)
        """,
        (elapsed_seconds, timestamp)
    )
    connection.commit()

    connection.close()

def add_timer_record(amount_of_seconds_for_the_timer: int):
    timestamp = datetime.now().timestamp()

    connection = connect(DATA_BASE_FILE)
    cursor = connection.cursor()

    try:
        cursor.execute(
            """
            CREATE TABLE timer(
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

    cursor.execute(
        """
        INSERT INTO timer(seconds, date) VALUES (?, ?)
        """,
        (amount_of_seconds_for_the_timer, timestamp)
    )
    connection.commit()

    connection.close()


def get_stats():
    pass


@ck.command
def show_stats():
    ck.echo("Hello world!")
