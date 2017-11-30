# List to string is a scipt that pastes in a list from the clipboard and converts
# it to an actual string.

import pyperclip

text = pyperclip.paste()


def convert_text(text):
    return " ".join(text.split())

# Copy the joined list back to the clipboard
pyperclip.copy(convert_text(text))
