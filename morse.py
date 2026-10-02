"""Morse code encoder/decoder. No dependencies; works on Python 3.8+."""

MORSE = {
    "A": ".-",    "B": "-...",  "C": "-.-.",  "D": "-..",
    "E": ".",     "F": "..-.",  "G": "--.",   "H": "....",
    "I": "..",    "J": ".---",  "K": "-.-",   "L": ".-..",
    "M": "--",    "N": "-.",    "O": "---",   "P": ".--.",
    "Q": "--.-",  "R": ".-.",   "S": "...",   "T": "-",
    "U": "..-",   "V": "...-",  "W": ".--",   "X": "-..-",
    "Y": "-.--",  "Z": "--..",
    "0": "-----", "1": ".----", "2": "..---", "3": "...--",
    "4": "....-", "5": ".....", "6": "-....", "7": "--...",
    "8": "---..", "9": "----.",
    ".": ".-.-.-", ",": "--..--", "?": "..--..", "'": ".----.",
    "!": "-.-.--", "/": "-..-.", "(": "-.--.",  ")": "-.--.-",
    "&": ".-...",  ":": "---...", ";": "-.-.-.", "=": "-...-",
    "+": ".-.-.",  "-": "-....-", "_": "..--.-", '"': ".-..-.",
    "$": "...-..-", "@": ".--.-.",
}
REVERSE = {code: ch for ch, code in MORSE.items()}

WORD_GAP = " / "   # words separated by " / ", letters by a single space


def encode(text: str) -> str:
    """Encode text to Morse code. Unknown characters are skipped."""
    words = []
    for word in text.upper().split():
        letters = [MORSE[ch] for ch in word if ch in MORSE]
        if letters:
            words.append(" ".join(letters))
    return WORD_GAP.join(words)


def decode(morse: str) -> str:
    """Decode Morse code back to text. Unknown sequences become '?'."""
    words = []
    for word in morse.strip().split(" / "):
        letters = [REVERSE.get(code, "?") for code in word.split()]
        words.append("".join(letters))
    return " ".join(words)
