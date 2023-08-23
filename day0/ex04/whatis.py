import sys
argv = sys.argv[1:]
try: 
    try:
        assert len(argv) < 2, "more than one argument is provided"
        number = int(argv[0])
        print("I'm Odd.") if number % 2 else print("I'm  Even.")
    except ValueError :
        raise AssertionError("argument is not an integer")
    except IndexError :
        None
except AssertionError as e:
    print(f'AssertionError: {e}')

