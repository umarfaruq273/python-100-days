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

#backslash escape a character
print('\' and \"')

#backlslash escape a backslash
print('C:\\Program Files')

#octal character
print('\0', '\1', '\2', '\3', '\4', '\5')
print('\120', '\121', '\122', '\123', '\124', '\125')
print('\255', '\256', '\257', '\258', '\259', '\26', '\27')

#hexadecimal character
print('\x50', '\x51', '\x52', '\x53', '\x54', '\x55')

#named unicode character
print('\N{LATIN CAPITAL LETTER P}')
print('\N{SNAKE}')

#bytes literal
print(b'\x89PNG\r\n\x1a\n')
print(list(b'\x89PNG\r\n\x1a\n'))

#f-strings
who = 'nobody'
nationality = 'Spanish'
print(f'{who.title()} expects the {nationality} Inquisition!')
print(f'{{...}}')


