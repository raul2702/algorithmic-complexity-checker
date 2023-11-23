import ast
import re

def get_function_text(file, func):
    with open(file, 'r') as code:
        in_func = False
        func_lines = []
        indentation = 0
        for line in code:
            if re.search(fr"def {func}\(", line):
                in_func = True
                indentation = len(line) - len(line.lstrip())
                func_lines.append(line)
            elif in_func:
                #if re.search(r"def", line): 
                #    break
                if line.lstrip() == '':
                    continue
                indentation_in_func = len(line) - len(line.lstrip())
                if indentation_in_func <= indentation:
                    break
                func_lines.append(line)
    return func_lines

def clean_function(func):
    first_identation = 0 
    indentation = 0
    clean_list = []
    for i, element in enumerate(func):
        if i == 0:
            indentation = len(element) - len(element.lstrip())
        if indentation == 0:
            return func
        clean_list.append(element[indentation:])
        
    return clean_list
        
def find_fors(func):
    tree = ast.parse(func)

    fors = []

    for node in ast.walk(tree):
        if isinstance(node, ast.For):
            for_content = ast.get_source_segment(func, node)
            fors.append((node, for_content))

    return fors


