import re
print("\033[32mMatthew's ASCII converter.\033[0m")

types = {'d': "decimal", 'b': "binary", 'c': "character"}
inp = None

def valid(prompt, check):
  for _ in range(3):
    print(prompt)
    inp = input("Input: ")
    for i in check:
      if eval(i.replace('_', f"'{inp}'")):
        print()
        return inp
    else:
      print("\033[31mInvalid Input.\033[0m\n")
  print("\033[31mToo many Invalid Inputs.\033[0m")
  quit()
  
def output(outType):
  print(f"Input - {types[typee]}: '{inp}'")
  print(f"Output type - {types[outType]}\n")

typee = valid(
    f"Enter input type ({', '.join([f'{key}: {value}' for key, value in types.items()])}): ",
    ["_ == 'd'", "_ == 'b'", "_ == 'c'"]
)
print(f"Input type - {types[typee]}")
inp = valid("Enter input", [f"'{typee}' == 'd' and _.isdigit() and 0<=int(_)<=1114111", f"'{typee}' == 'b' and bool(re.match('^[01 ]+$', _)) and 0<=int(_.replace(' ',''), 2)<=1114111", f"'{typee}' == 'c' and len(_) <= 1"])
if typee == "d":
  output('c')
  print("\033[34m" + chr(int(inp)) + "\033[0m")
elif typee == "b":
  output('c')
  print("\033[34m" + chr(int(inp.replace(' ',''), 2)) + "\033[0m")