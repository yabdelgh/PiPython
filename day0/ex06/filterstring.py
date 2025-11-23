import sys
from ft_filter import ft_filter


def format(argv):
    """
        format argv
    """
    assert len(argv) == 3, "AssertionError: the arguments are bad"
    try:
        return [argv[1], int(argv[2])]
    except AssertionError:
        assert False, "AssertionError: the arguments are bad"


def main():
    """
        main
    """
    argv = format(sys.argv)
    words = argv[0].split(" ")
    tmp = ft_filter(lambda word: len(word) > argv[1], words)
    print([x for x in tmp])
    return 0


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
