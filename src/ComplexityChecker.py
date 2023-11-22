import re

import Utils 
 
class ComplexityChecker:
    def __init__(self, file, func):
        self.file = file
        self.func = func
        
    def On_algorithmic_complexity(self):
        pattern = re.compile(r'\b(?:for|while)\b')
        function_content = Utils.get_function_text(self.file, self.func)
        clean_function_content = Utils.clean_function(function_content)
        function_as_string = ''.join(clean_function_content)
        
        found_fors = Utils.find_fors(function_as_string)
        biggest_complexity = 0

        for found_for in found_fors:
            complexity = 0
            found_for_list = found_for[1].split("\n")
            for element in found_for_list:
                if pattern.search(element):
                    complexity = complexity + 1
            if complexity > biggest_complexity:
                biggest_complexity = complexity

        return biggest_complexity
    
func = "On_algorithmic_complexity"
#file= "/Users/bryaguir/Documents/Info_personal/Master/Diseño de algoritmos/CC_project/algorithmic-complexity-checker/test_scripts/test_script_On_complex.py"
file = "/Users/bryaguir/Documents/Info_personal/Master/Diseño de algoritmos/CC_project/algorithmic-complexity-checker/src/ComplexityChecker.py"

test = ComplexityChecker(file, func)
print(test.On_algorithmic_complexity())