"""Smoke tests for the Morse Code Toolkit. Run: python tests.py"""

from morse import decode, encode

# Round-trips
assert encode("SOS") == "... --- ..."
assert decode("... --- ...") == "SOS"

assert encode("hello world") == ".... . .-.. .-.. --- / .-- --- .-. .-.. -.."
assert decode(".... . .-.. .-.. --- / .-- --- .-. .-.. -..") == "HELLO WORLD"

assert decode(encode("Morse code 123!")) == "MORSE CODE 123!"

# Lowercase input is fine
assert encode("sos") == "... --- ..."

# Unknown characters are skipped when encoding, unknown sequences -> "?" when decoding
assert encode("~sos") == "... --- ..."
assert decode("........") == "?"

print("All tests passed.")
