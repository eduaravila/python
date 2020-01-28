a = "1"

print(type(a))


print(len(a))

my_name = "Eduardo"
print(my_name[1])
print(my_name[2:])
print(my_name[:2])
print(my_name[::])
print(my_name[::2])
print(my_name[::-1])
print(my_name[-1])

my_name_split = my_name.split("d")
print(my_name_split)

# * string formating

# ? placeholders

print("some thing here %s  or my name: %s" % ("hello", my_name))

print("/r print the string as a literal not representing the string or the simbols: %r" % ("\thello"))
print("/s print the string representing al the simbols passed: %s" %
      ("\thello\nsome jump "))
print("/d print the decimal numbers: %d" % (10))
print("/f print the floating point number: %f" % (10.198))

three_decimals = 10.123

print("Just prints 2 decimals %2.2f" % (three_decimals))

# ? formating

print("Some formating example: {}".format("example"))
print("Some formating example called with index: {0} {1}".format(
    "#1 example", "#2 example"))
print("Some formating example called with keywords : {p} {s}".format(
    p="#1 example", s="#2 example"))
print("Some formating example called with keywords : {p:.<20} | {s:.>20}".format(
    p="#1 example", s="#2 example"))

name = 'some f formating x2'
print(f"some f formating example {name}")

decimal_f_formating = 10.121
print(f"some decimal now: {decimal_f_formating:{1}.{6}}")
