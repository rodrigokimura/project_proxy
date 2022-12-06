import logging
import sys
from typing import Any

from colorama import Fore, Style
from proxy import Proxy, sleep_loop

LV = "●"
TS = "%(asctime)s"
PID = "%(process)d"
CODE = "%(module)s.%(funcName)s:%(lineno)d"


class CustomHandler(logging.StreamHandler):
    FMT = f"{Style.DIM}{TS} {PID} {Style.NORMAL}{CODE}{Style.DIM} - {Style.RESET_ALL}{Style.BRIGHT}%(message)s {Style.RESET_ALL}"

    FORMATS = {
        logging.DEBUG: f"{Fore.BLUE}{LV}{Style.RESET_ALL} " + FMT,
        logging.INFO: f"{Fore.WHITE}{LV}{Style.RESET_ALL} " + FMT,
        logging.WARNING: f"{Fore.YELLOW}{LV}{Style.RESET_ALL} " + FMT,
        logging.ERROR: f"{Fore.RED}{LV}{Style.RESET_ALL} " + FMT,
        logging.CRITICAL: f"{Fore.CYAN}{LV}{Style.RESET_ALL} " + FMT,
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)


logging.basicConfig(level=logging.DEBUG, handlers=[CustomHandler()])


def main(**opts: Any) -> None:
    with Proxy(sys.argv[1:], **opts):
        sleep_loop()


if __name__ == "__main__":
    main()
