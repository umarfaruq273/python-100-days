#string literal
x = "spam"
y = 'eggs'
print(x, y)
print(x+y)
print("x " + 'y')
print('1 - Say "Hello", please.'"Don't do that!")
print('2 - Say "Hello", please.',"Don't do that!")
print('3 - Say "Hello", please.', "Don't do that!")
print('4 - Say "Hello", please.'
      "Don't do that!")

#bytes literal
print(b'\x89PNG\r\n\x1a\n')
print(list(b'\x89PNG\r\n\x1a\n'))

#f-strings
who = 'nobody'
nationality = 'Spanish'
print(f'{who.title()} expects the {nationality} Inquisition!')
print(f'{{...}}')


