#string literal
x = "spam"
y = 'eggs'
print(x, y)
print(x+y)
print("x " + 'y')

#Another way of using quote in strings
print('1 - Say "Hello", please.'"Don't do that!")
print('2 - Say "Hello", please.',"Don't do that!")
print('3 - Say "Hello", please.', "Don't do that!")
print('4 - Say "Hello", please.'
      "Don't do that!")
print("5 - Say \"Hello\" to everyone!")

#Triple-quoted strings
print("""6 - This is a triple-quoted string.""")
print("""7 - This string has "quotes" inside.""")
print('''8 - This triple-quoted string
continues on the next line.''')

#Using backslash in strings by ignoring newline
print('This string will not include \
backslashes or newline characters.')

#backlslash escape a backslash
print('C:\\Program Files')

#bytes literal
print(b'\x89PNG\r\n\x1a\n')
print(list(b'\x89PNG\r\n\x1a\n'))

#f-strings
who = 'nobody'
nationality = 'Spanish'
print(f'{who.title()} expects the {nationality} Inquisition!')
print(f'{{...}}')


