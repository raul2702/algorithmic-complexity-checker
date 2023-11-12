import argparse


def main():
    parser = argparse.ArgumentParser(description='This program will check the algorithmic complexity of a python code')

    parser.add_argument('--file_check', '-fic', type=str, help='This parameter is used to check the algorithmic complexity of the provided .py file')
    parser.add_argument('--function_check', '-fuc', type=str, help='This parameter is used to check the algorithmic complexity of an specific funcion of the provided .py file')

    args = parser.parse_args()

    if args.file_check:
        file_check(args.file_check)
    elif args.function_check:
        function_check(args.function_check)
    else:
        print('Choose one of the following parse arguments: \n\t--file-check, -fic \n\t--function-check, -fuc')

def file_check(arg):
    print(arg)
    pass

def function_check(arg):
    print(arg)
    pass

if __name__ == "__main__":
    main()