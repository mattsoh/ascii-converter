import os, re
types = {'d': "decimal", 'b': "binary", 'c': "character"}
inp = None

print("\033[32mMatthew's ASCII converter.\033[0m")
 
def valid(prompt, check):
  for _ in range(3):
    print(prompt)
    inp = input("Input: ")
    for i in check:
      if eval(i.replace('_', f"'{inp}'")):
        print()
        return inp
    else:
      os.system('clear' if os.name == 'posix' else 'cls')
      print("\033[31mInvalid Input.\033[0m\n")
  os.system('clear' if os.name == 'posix' else 'cls')
  print("\033[31mToo many Invalid Inputs.\033[0m")
  quit()
 
def output(outType):
  os.system('clear' if os.name == 'posix' else 'cls')
  print(f"Input - {types[typee]}: '{inp}'")
  print(f"Output type - {types[outType]}\n")
 
os.system('clear' if os.name == 'posix' else 'cls')
typee = valid(f"Enter input type ({', '.join([f''''{key}': {value}''' for key, value in types.items()])})", ["_ == 'd'","_ == 'b'","_ == 'c'"])
os.system('clear' if os.name == 'posix' else 'cls')
print(f"Input type - {types[typee]}")
inp = valid("Enter input", [f"'{typee}' == 'd' and _.isdigit() and 0<=int(_)<=1114111", f"'{typee}' == 'b' and bool(re.match('^[01 ]+$', _)) and 0<=int(_.replace(' ',''), 2)<=1114111", f"'{typee}' == 'c' and len(_) <= 1"])
if typee == "d":
  output('c')
  print("\033[34m" + chr(int(inp)) + "\033[0m")
elif typee == "b":
  output('c')
  print("\033[34m" + chr(int(inp.replace(' ',''), 2)) + "\033[0m")
elif typee == "c":
  os.system('clear' if os.name == 'posix' else 'cls')
  outType = valid(f"Enter output type ({', '.join([f''''{key}': {value}''' for key, value in list(types.items())[:2]])})", ["_ == 'd'","_ == 'b'"])
  output(outType)
  if outType == "d":
    print("\033[34m" + str(ord(inp)) + "\033[0m")
  elif outType == "b":
    print("\033[34m" + ' '.join(re.findall('........', format(ord(inp),'08b'))) + "\033[0m")