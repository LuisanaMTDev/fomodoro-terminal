import curses
from curses import wrapper
from time import sleep, strftime, gmtime
from json import load, dump

from fomodoro.utils import States, SECONDS_FORMAT, INFO_FILE
from fomodoro.stopwatch import Stopwatch


stopwatch_obj = Stopwatch()

def main(stdscr):
    """"""
    with open(INFO_FILE, 'r', encoding='utf-8') as info_file:
        info = load(info_file)

    if info["stopwatch_state"] == 'Pause' or info["stopwatch_state"] == " ":
        stopwatch_obj.start()
        stopwatch_obj.elapsed_seconds = info["elapsed_seconds"]
        time_window = curses.newwin(1, 10, 12, 55)

        while stopwatch_obj.state is States.START:
            sleep(1.0)
            stopwatch_obj.elapsed_seconds += 1
            stopwatch_obj.seconds += 1
            struct_time = gmtime(float(stopwatch_obj.elapsed_seconds))
            formated_seconds = strftime(SECONDS_FORMAT, struct_time)

            time_window.nodelay(True)
            time_window.clear()
            time_window.addstr(formated_seconds[0:], curses.A_BOLD)
            time_window.refresh()
            try:
                character = time_window.getkey()
                if character == "p":
                    stopwatch_obj.state = States.PAUSE
                    info["stopwatch_state"] = 'Pause'
                    info["elapsed_seconds"] = info["elapsed_seconds"] + stopwatch_obj.seconds
                    with open(INFO_FILE, 'w', encoding='utf-8') as info_file:
                        dump(info, info_file, indent=2)
                elif character == "s":
                    stopwatch_obj.state = States.STOP
                    info["stopwatch_state"] = 'Stop'
                    info["elapsed_seconds"] = info["elapsed_seconds"] + stopwatch_obj.seconds
                    with open(INFO_FILE, 'w', encoding='utf-8') as info_file:
                        dump(info, info_file, indent=2)
            except curses.error:
                character = None
    else:
        #TODO: Timer
        pass


wrapper(main)
