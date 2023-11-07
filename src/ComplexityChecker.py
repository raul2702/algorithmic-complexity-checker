import argparse


def main():
    parser = argparse.ArgumentParser(description='This program will check the algorithmic complexity of a python code')

    parser.add_argument('--file_check', '-fic', type=str, help='This parameter is used to check the algorithmic complexity of the provided .py file')
    file_check()

    parser.add_argument('--function_check', '-fuc', type=str, help='This parameter is used to check the algorithmic complexity of an specific funcion of the provided .py file')
    function_check()

    args = parser.parse_args()
    #print(f'hola: {args.file_check}')


def file_check():
    pass

def function_check():
    pass

if __name__ == "__main__":
    main()