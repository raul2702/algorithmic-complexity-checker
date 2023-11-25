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

    def logarithmic_complexity(self):
        """
        Check if the complexity is logarithmic O(Log N)
        """
        function_content = Utils.get_function_text(self.file, self.func)
        clean_function_content = Utils.clean_function(function_content)
        function_as_string = ''.join(clean_function_content)
        patron = re.compile(r'\bwhile\b.*\b(\w+)\s*=\s*(\w+)\s*([*/])\s*2\b|\bfor\b.*\bin\b\s*\brange\b.*\b\w+\b\s*([*/])\s*2', re.DOTALL)
        resultado = patron.search(function_as_string)
        if resultado:
            print("Algoritmo de complejidad logaritmica.")
        else:
            print("El Algoritmo no es complejidad logaritmica.")
