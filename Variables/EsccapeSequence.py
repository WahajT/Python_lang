#  Escape Sequences allow you to put special characters such as the tab, the new line, and the backspace (delete key) into your strings. The following table showcases the escape sequence character and description.

# \b  Backspace
# \a  Sound system bell
# \n  newline
# \t  horizontal tab
# \'  Singel quotates
# \""  Double quotates
# \\  the \ character

print('\a')
print ('\t\t Python' )
print ('i know , you are \'magnificent\'')

# Python allows you to set a formatted output. If you have done some coding in C language, then you must be familiar with %d, %f, %s. To represent int, float and string %d, %f and %s are used respectively.
# See the following program.
print ("Name Marks Age" )
print ( "%s %14.2f %11d" % ("Mohit", 80.67, 27))
print ( "%s %12.2f %11d" %("Bhaskar" ,76.907, 27))
print ( "%s %3.2f %11d" %("Nitin Shelke", 56.983, 25))