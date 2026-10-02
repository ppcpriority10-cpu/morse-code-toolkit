# Morse Code Toolkit

A tiny, dependency-free Python toolkit for encoding text to Morse code and decoding Morse code back to text. Good for learning the code, experimenting in a notebook, or embedding in small projects.

## Features

- Encode plain text (A–Z, 0–9, common punctuation) to Morse code
- Decode Morse code back to readable text
- Simple CLI: `python cli.py encode "hello world"`
- No dependencies — runs on any Python 3.8+

## Quick start

```bash
# Encode text to Morse
python cli.py encode "SOS"

# Decode Morse to text
python cli.py decode "... --- ..."

# Or use it in your own code
from morse import encode, decode
print(encode("hello"))        # .... . .-.. .-.. ---
print(decode(".... . .-.. .-.. ---"))  # hello
```

## Try it in your browser

If you'd rather not run any code, there's a free online tool for this:
[Morse Code Translater](https://www.morsecodetranslater.com/) — type text and hear it played as Morse, or decode Morse back to text. It also has a full [morse code alphabet reference](https://www.morsecodetranslater.com/morse-code-alphabet) with every letter, number, and punctuation mark.

## License

MIT — use it however you like.
