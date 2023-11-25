import re
import Utils 
 
class ComplexityChecker:
    def __init__(self, file, func):
        self.file = file
        self.func = func
        
    def On_algorithmic_complexity(self):
        #pattern = re.compile(r'\b(?:for|while)\b')
        pattern = re.compile(r'^\s*(for|while)\s')
        function_content = Utils.get_function_text(self.file, self.func)
        clean_function_content = Utils.clean_function(function_content)

        function_as_string = ''.join(clean_function_content)

        found_loops = Utils.find_fors_and_whiles(function_as_string)
        biggest_complexity = 0
        log = False
        for found_loop in found_loops:
            complexity = 0
            found_for_list = found_loop[1].split("\n")
            for element in found_for_list:
                if pattern.search(element):
                    complexity = complexity + 1
            if complexity > biggest_complexity:
                biggest_complexity = complexity
                log = self.logarithmic_complexity(found_loop[1])

        return biggest_complexity, log

    def logarithmic_complexity(self, text):
        """
        Check if the complexity is logarithmic O(Log N)
        """
        pattern = re.compile(r'\bwhile\b.*\b(\w+)\s*=\s*(\w+)\s*([*/])\s*2\b|\bfor\b.*\bin\b\s*\brange\b.*\b\w+\b\s*([*/])\s*2', re.DOTALL)
        result = pattern.search(text)
        if result:
            return True
        else:
            return False
