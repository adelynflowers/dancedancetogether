"""Driver file for DanceDanceTogether.
"""
from dancedancetogether.controllers import register_event_loop


def main():
    """
    Entrypoint, does nothing.
    """
    register_event_loop()
    while True:
        ...


if __name__ == "__main__":
    main()
