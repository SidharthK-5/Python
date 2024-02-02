"""
Built-in fns for str
print(dir(str)) gives the list of fns in str datatype
"""

print("String formatting")
num1 = 100
num2 = 200
print(f"{num1=} {num2=}")
print(
    "Value of num1 is {} value of num2 {}".format(num1, num2)
)  # Placing num1 and num2 in order
print(
    "Value of num2 is {1} value of num1 {0}".format(num1, num2)
)  # Placing num1 in position 0 and num2 in position 1 (by specifying index)
print(
    "Value of num1 is {val1} value of num2 {val2}".format(val1=num1, val2=num2)
)  # Passing right value at right location

print("\ncapitalize() function")
string = "python sample string"
print(f"{string=}")
string_1 = string.capitalize()
print(f"string capitalized: {string_1}")

print("\ntitle() function")
print(f"string converted to title: {string.title()}")
print(f"Checking if {string=} is a title: {string.istitle()}")

print("\nsplit() and join()")
string_2 = "HTML,CSS,PYTHON,JAVA,Django"
print(f"{string_2=}")
sample_list = string_2.split(",")
print(f"string_2 split at ',': {sample_list}")
string_3 = " ".join(sample_list)
print(f"sample_list joined togather with ' ': {string_3}")

print("\nmaketrans() and translate()")
original_text = "abcd"
translation = "1234"
sentence = "Python Sample string abcd"
print(f"{sentence=}")

translation_table = str.maketrans(original_text, translation)
print(f"{translation_table=}   --> This is the ASCII representaion of translation")
sentence_translated = sentence.translate(translation_table)
print(f"{sentence_translated=}")

print("\nindex(), find() and rfind()")
languages = "HTML,CSS,PYTHON,PYTHON,PYTHON"
print(f"{languages=}")
print("Checking if 'PYTHON' is present in languages", end=": ")
print("PYTHON" in languages)

"""
index() will show error if item is not found. find() will return -1 for the same case
rfind() will return the highest index of the string there substring is found
"""
print(f"index of PYTHON in languages: {languages.index('PYTHON')}")
print(f"index using find(): {languages.find('PYTHON')}")
print(f"Highest index of 'PYTHON' in languages: {languages.rfind('PYTHON')}")

print("\nstrip(), lstrip(), rstrip()")
base_string = "@@@@SAMPLE STRING+++++"
print(f"{base_string=}")
print(f"Stripping '@' from left of base_string: {base_string.lstrip('@')}")
print(f"Stripping '+' from right of base_string: {base_string.rstrip('+')}")

print("\ncenter(), ljust(), rjust()")
base_string = "python"
print(f"{base_string=}")
print(f"Using center(): {base_string.center(20, '*')}")
print(f"Using ljust(): {base_string.ljust(20, '*')}")
print(f"Using rjust(): {base_string.rjust(20, '*')}")

print("\nreplace()")
languages = "html,css,python,html"
new_languages = languages.replace("html", "HTML5")
print(f"{languages=}")
print(f"Languages after replacing 'html' with 'HTML5': {new_languages}")
