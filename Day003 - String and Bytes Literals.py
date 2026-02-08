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

#hexadecimal unicode character
print('\u1234', '\U0001f40d')

#unrecognized escape sequences
print('\q')
print(list('\q'))

#bytes literal
print(b'\x89PNG\r\n\x1a\n')
print(list(b'\x89PNG\r\n\x1a\n'))

#f-strings
who = 'nobody'
nationality = 'Spanish'
print(f'{who.title()} expects the {nationality} Inquisition!')
print(f'{{...}}')

#expressions in formatted strings
print(f'{(half := 1/2)}, {half * 42}')
print(f'{(half := 1/2)}, {half * 42}')

#reusing outer f-string quoting type inside a replacement field
a = dict(x=2)
print(f"abc {a["x"]} def")

#backslash is allowed in replacement field
a = ["a", "b", "c"]
print(f"List a contains:{"\n".join(a)}")
print(f"List a contains:\n{"\n".join(a)}")

#nest f-string
#CPython does not limit nesting of f-strings.
#Portable Python programs should not use more than 5 levels of nesting
name = 'world'
print(f'Repeated:{f' hello {name}' * 3}')

#numeric literal
10.  # (equivalent to 10.0)
.001  # (equivalent to 0.001)
1.0e3  # (represents 1.0×10³, or 1000.0)
1.166e-5  # (represents 1.166×10⁻⁵, or 0.00001166)
6.02214076e+23  # (represents 6.02214076×10²³, or 602214076000000000000000.)
1e3  # (equivalent to 1.e3 and 1.0e3)
0e0  # (equivalent to 0.)
3+4.2j # imaginary literal end with character "j"
# valid examples of imaginary literal
4.2j
3.14j
10.j
.001j
1e100j
3.14e-10j
3.14_15_93j

#operators and delimiters
OP:
   | assignment_operator
   | bitwise_operator
   | comparison_operator
   | enclosing_delimiter
   | other_delimiter
   | arithmetic_operator
   | "..."
   | other_op

assignment_operator:   "+=" | "-=" | "*=" | "**=" | "/="  | "//=" | "%=" |
                       "&=" | "|=" | "^=" | "<<=" | ">>=" | "@="  | ":="
bitwise_operator:      "&"  | "|"  | "^"  | "~"   | "<<"  | ">>"
comparison_operator:   "<=" | ">=" | "<"  | ">"   | "=="  | "!="
enclosing_delimiter:   "("  | ")"  | "["  | "]"   | "{"   | "}"
other_delimiter:       ","  | ":"  | "!"  | ";"   | "="   | "->"
arithmetic_operator:   "+"  | "-"  | "**" | "*"   | "//"  | "/"   | "%"
other_op:              "."  | "@"

