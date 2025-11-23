import sys

morseCode = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..',
    'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...',  'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--',  'X': '-..-',
    'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....', '6': '-....',
    '7': '--...', '8': '---..', '9': '----.', '0': '-----', ' ': '/'
}


def isAlphaNumSpa(_str):
    """
        only alphas, nums or spaces
    """
    return all(char.isalnum() or char.isspace() for char in _str)


def main() -> int:
    """
        main
    """
    _str = str()
    assert len(sys.argv) == 2, "AssertionError: the arguments are bad"
    assert isAlphaNumSpa(sys.argv[1]), "AssertionError: the arguments are bad"
    for char in sys.argv[1].upper():
        _str += morseCode[char] + ' '
    print(_str.strip())
    return 0


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
