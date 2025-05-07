# Inputs...
# Variables
first_name = input('What is your First Name\n')
fav_prog_lang= input('What is your favorite programming language\n')

# Outputs...
print(f'Nice to meet you {first_name}! {fav_prog_lang} is a great choice!')
print(f'Your name has {len(first_name)} characters.')

print(f'{first_name.upper()}') # Print all uppercase (which is called a method)
print(fav_prog_lang[::-1]) # Print in reverse using slicing