my_name = "molly"

letters_list = [letter for letter in my_name]
print(letters_list)

double_list = [number * 2 for number in range(1,5)]
print(double_list)

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
short_names = [name for name in names if len(name) < 5]
print(short_names)

uppercase_names = [name.upper() for name in names if len(name) > 5]
print(uppercase_names)