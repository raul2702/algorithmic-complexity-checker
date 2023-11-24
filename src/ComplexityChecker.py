import argparse


def main():
    parser = argparse.ArgumentParser(description='This program will check the algorithmic complexity of a python code')

    parser.add_argument('--file', '-f', type=str, help='This parameter is used to identify .py file of the function')
    parser.add_argument('--function-to-check', '-func', type=str, help='This parameter is used to check the algorithmic complexity of an specific funcion of the provided .py file')

    args = parser.parse_args()

    if args.function_check and args.file:
        function_check(args.function_check)
    else:
        print('Type the following parse arguments: \n\t--file, -f \n\t--function-to-check, -func')

def function_check(arg):
    print(arg)
    pass

if __name__ == "__main__":
    main()
