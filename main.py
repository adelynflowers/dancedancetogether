"""Driver file for DanceDanceTogether.
"""
from dancedancetogether.controllers import JoystickManager
from loguru import logger


def print_input(joy, key):
    print(f"Joystick {joy.identifier} pressed {key.name}")


@logger.catch
def main():
    """
    Entrypoint, does nothing.
    """
    joystick_manager = JoystickManager()
    joystick_manager.register_callback(print_input)
    while True:
        ...


if __name__ == "__main__":
    main()
