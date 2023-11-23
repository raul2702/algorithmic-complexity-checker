from ComplexityChecker import ComplexityChecker

func = "On_algorithmic_complexity"
#file= "/Users/bryaguir/Documents/Info_personal/Master/Diseño de algoritmos/CC_project/algorithmic-complexity-checker/test_scripts/test_script_On_complex.py"
file = "/Users/bryaguir/Documents/Info_personal/Master/Diseño de algoritmos/CC_project/algorithmic-complexity-checker/src/ComplexityChecker.py"

test = ComplexityChecker(file, func)
print(test.On_algorithmic_complexity())