#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv[1:]
    args_num = len(argv)

    if args_num == 0:
        print("0 arguments.")

    elif args_num == 1:
        print("1 argument:")
        print("1: {}".format(argv[0]))
    else:
        print("{} arguments:".format(args_num))
        for i, arg in enumerate(argv, start=1):
            print("{}: {}".format(i, arg))
