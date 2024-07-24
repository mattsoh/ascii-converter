# Step 3: Refactor Validation into a Function

print("\033[32mMatthew's ASCII converter.\033[0m")

types = {'d': "decimal", 'b': "binary", 'c': "character"}

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
typee = valid(
    f"Enter input type ({', '.join([f'{key}: {value}' for key, value in types.items()])}): ",
    ["_ == 'd'", "_ == 'b'", "_ == 'c'"]
)
print(f"Input type - {types[typee]}")
