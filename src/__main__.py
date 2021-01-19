from os import sys
from color_console import CONSOLE_COLORS
import win_register as hkey

def _cprint(color: str, text: str):
    sys.stdout.write(color + text + CONSOLE_COLORS.RESET.value)


def _cprintLine(color: str, text: str):
    sys.stdout.write(color + text + CONSOLE_COLORS.RESET.value + '\n')


if __name__ == "__main__":
	hkey.verify_register()
