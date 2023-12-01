# algorithmic-complexity-checker
In this repository we will make a python code that will check the complexity.

Instructions:
    To execute this script and analize the complexity of a python function,
    It is necessary to execute the main.py file, the script is using a python 
    library called "argparse". this library allows us to send parameters using 
    the CLI. you can find more details with this command:
    python3 main.py --help

    Examples:
    There is an example file in the repository: test_script_On_complex.py
    example1:
    python3 main.py --file "/Users/bryaguir/Documents/Info_personal/Master/Diseño de algoritmos/CC_project/algorithmic-complexity-checker/test_scripts/test_script_On_complex.py" --function_to_check "take_concurrent_node_dump"
    example2:
    python3 main.py -f "/Users/bryaguir/Documents/Info_personal/Master/Diseño de algoritmos/CC_project/algorithmic-complexity-checker/test_scripts/test_script_On_complex.py" -func "n_log_n"
