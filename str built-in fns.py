""" Built-in fns for str
print(dir(str)) gives the list of fns in str datatype"""

print("format function")
num1 = 100
num2 = 200
print("Value of num1 is {} value of num2 {}".format(num1, num2))
print("Value of num2 is {1} value of num1 {0}".format(num1, num2))
print("Value of num1 is {val1} value of num2 {val2}".format(val1=num1, val2=num2))

print("\ncapitalize function")
s = "python sample string"
print(s)
s1 = s.capitalize()
print(s1)

print("\ntitle function")
print(s.title())
print(s.istitle())

print("\nsplit and join")
s2 = "HTML,CSS,PYTHON,JAVA,Django"
print(s2)
l = s2.split(",")
print(l)
s3 = " ".join(l)
print(s3)

print("\nmaketrans and translate")
a1 = "abcd"
a2 = "1234"
a3 = "Python Sample string abcd"
print(a3)
table = str.maketrans(a1, a2)
result = a3.translate(table)
print(result)

print("\nindex, find and rfind")
b = "HTML,CSS,PYTHON,PYTHON,PYTHON"
print(b)
print("PYTHON" in b)
""" index will show error if item is not found. find will return -1 for
the same case"""
print(b.index("PYTHON"))
print(b.find("PYTHON"))
print(b.rfind("PYTHON"))

print("\nstrip, lstrip, rstrip")
c = "@@@@SAMPLE STRING+++++"
print(c)
print(c.lstrip("@"))
print(c.rstrip("+"))

print("\ncenter, ljust, rjust")
d = "python"
print(d)
print(d.center(20, "*"))
print(d.ljust(20, "*"))
print(d.rjust(20, "*"))

print("\nreplace")
e = "html,css,python,html"
e1 = e.replace("html", "HTML5")
print(e)
print(e1)
