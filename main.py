"""Driver file for DanceDanceTogether.
"""
from dancedancetogether.controllers import JoystickManager
from dancedancetogether.app import DDTApp
from loguru import logger


def print_input(joy, key):
    print(f"Joystick {joy.identifier} pressed {key.name}")


@logger.catch
def main():
    """
    Entrypoint, does nothing.
    """
    ddt = DDTApp()
    ddt.run()


if __name__ == "__main__":
    main()
