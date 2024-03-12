import keyboard, mouse, os

while True:
    # Wait for the next event.
    event = keyboard.read_event()
    if event.name != "space" and not event.name == "^":
        keyboard.press("a")
        keyboard.send("ctrl+alt+del")
        mouse.double_click()
    else:
        os._exit(0)
