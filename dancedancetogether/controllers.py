from pyjoystick.sdl2 import run_event_loop


def print_add(joy):
    print("Added", joy)


def print_remove(joy):
    print("Removed", joy)


def key_received(key):
    print("Key:", key)


def register_event_loop():
    run_event_loop(print_add, print_remove, key_received)
