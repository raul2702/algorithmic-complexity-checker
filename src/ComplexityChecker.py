import re

class ComplexityChecker:
    def __init__(self, file, func):
        self.file = file
        self.func = func

    def On_algorithmic_complexity(self):
        pattern = re.compile(r'\b(?:for|while)\b')
        function_content = self.get_function_text()

        indentation = 0
        complexity = 0
        biggest_identation = 0
        for element in function_content:
            if pattern.search(element):
                indentation = len(element) - len(element.lstrip())
                if indentation > biggest_identation:
                    biggest_identation = indentation
                    complexity = complexity + 1

        return complexity
    def get_function_text(self):
        with open(self.file, 'r') as code:
            in_func = False
            func_lines = []

            for line in code:
                if re.search(fr"def {self.func}\(", line):
                    in_func = True
                    func_lines.append(line)
                elif in_func:
                    if re.search(r"def", line): 
                        break 
                    func_lines.append(line)
        return func_lines

func = "take_node_snaps"
file= "/Users/bryaguir/Documents/Info_personal/Master/Diseño de algoritmos/CC_project/algorithmic-complexity-checker/test_scripts/test_script_On_complex.py"
test = ComplexityChecker(file, func)
print(test.On_algorithmic_complexity())