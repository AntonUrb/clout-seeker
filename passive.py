import sys

from fname_checker.main import fname_checker
from ip_checker.main import ip_checker
from username_checker.main import check


def save_file(input):
    counter = 1
    while True:
        file_name = f"result{'' if counter < 2 else counter}.txt"
        try:
            with open(file_name, 'x') as file:
                file.write(input)
            return file_name
        except FileExistsError:
            counter += 1


args = sys.argv[1:]

if __name__ == "__main__":
    result = None
    if args[0] == "-fn":
        names = args[1].split(" ")
        result = fname_checker(names[0], names[1])
    elif args[0] == "-ip":
        result = ip_checker(args[1])
    elif args[0] == "-u":
        result = check(args[1])
    elif args[0] == "--help":
        print("""Welcome to passive v1.0.0
OPTIONS:
    -fn         Search with full-name
    -ip         Search with ip address
    -u          Search with username""")
        exit()
    else:
        exit()
    filename = save_file(result)
    print(result)
    print("Saved in " + filename)


def ip_scan():
    pass


def fullname_scan():
    pass


def username_scan():
    pass
