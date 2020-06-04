import pyperclip
"""
Since pyperclip is not the python standard library so it should be installed to the system using the pip
command "pip install pyperclip" inside the command prompt(Applicable for windows only)

pyperclip has copy() and paste() function that can be used to copy any text and print it anywhere in the 
code line.
"""
pyperclip.copy('Copied Text')# Now the text has been copied
print(pyperclip.paste()) # The text is pasted in this line and displayed in console using the print function
copied_text = pyperclip.paste() # The copied text can be stored to any variable also
print(copied_text)