from pyjoystick.sdl2 import Key, Joystick, run_event_loop
from typing import Callable, Any
from loguru import logger
import threading


class JoystickManager:
    """
    Manages joystick input
    and relaying it to the rest of the
    program.
    """

    _joysticks: list[Joystick]

    _callbacks: dict[Joystick, list[Callable[[Joystick, Key], Any]]]

    def __init__(self):
        logger.debug("Initializing JoystickManager")
        self._joysticks = []
        self._callbacks = {}
        threading.Thread(target=self.register_event_loop).start()

    def add_joystick(self, joystick: Joystick) -> None:
        """
        Adds joystick to class upon detection.
        """
        logger.debug(f"Adding joystick {joystick.name}/{joystick.identifier}")
        self._joysticks.append(joystick)

    def remove_joystick(self, joystick: Joystick) -> None:
        """
        Removes joystick from class upon removal.
        """
        logger.debug(f"Removing joystick {joystick.name}/{joystick.identifier}")
        self._joysticks.remove(joystick)

    def register_callback(
        self, fn: Callable[[Joystick, Key], Any], joy: Joystick = None
    ) -> None:
        """
        Registers a callback function to be called when a
        key event is received.

        Args:
            fn (Callable[[Joystick, Key], Any]): Function that takes a Joystick and Key as input
            joy (Joystick, optional): Joystick to receive events for. Defaults to all joysticks.
        """
        logger.debug(f"Registering callback {fn} for joystick {joy}")
        if joy not in self._callbacks:
            self._callbacks[joy] = []
        self._callbacks[joy].append(fn)

    def key_received(self, key: Key) -> None:
        """
        Handler for key events from pyjoystick.
        """
        joy = key.joystick
        logger.debug(f"{key} pressed on joystick {joy}")
        if joy in self._callbacks:
            for callback in self._callbacks[joy]:
                callback(joy, key)
        for callback in self._callbacks[None]:
            callback(joy, key)

    def register_event_loop(self) -> None:
        run_event_loop(self.add_joystick, self.remove_joystick, self.key_received)
