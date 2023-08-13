import sys

def main() -> int :
    argv = sys.argv
    calc = {"upper": 0, "lower": 0, "punctuation": 0, "spaces": 0, "digits": 0}
    assert len(argv) < 3, "Incorrect number of arguments. Expected: single string"
    if len(argv) < 2 : 
        print("What is the text to count?")
        tmp = sys.stdin.readline() 
    else :
        tmp = argv[1]
    for char in tmp :
        if char.isupper() : calc["upper"] += 1
        elif char.islower() : calc["lower"] += 1
        elif char.isdigit() : calc["digits"] += 1
        elif char.isspace() : calc["spaces"] += 1
        else : calc["punctuation"] += 1
    print(f"The test contains {len(tmp)} characters:\n{calc['upper']} upper letters\n{calc['lower']} lower letters")
    print(f"{calc['punctuation']} punctuation marks\n{calc['spaces']} spaces\n{calc['digits']} digits")
    return 0


if __name__ == "__main__":
    try: 
        main()
    except Exception as e:
        print(f"Error: {e}")