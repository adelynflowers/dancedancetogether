from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Static
from typing import Generator
from dancedancetogether.controllers import JoystickManager

READY_P1_STR = "Press a button on the controller you want to be P1"


class DDTApp(App):
    """A Textual app to manage stopwatches."""

    current_text: str
    BINDINGS = [("d", "toggle_dark", "Toggle dark mode")]

    joystick_manager: JoystickManager

    def __init__(self):
        self.current_text = READY_P1_STR
        self.joystick_manager = JoystickManager()

    def compose(self) -> ComposeResult | Generator:
        """Create child widgets for the app."""
        yield Header()
        yield Static(self.current_text)
        yield Footer()

    def action_toggle_dark(self) -> None:
        """An action to toggle dark mode."""
        self.dark = not self.dark

    def 
