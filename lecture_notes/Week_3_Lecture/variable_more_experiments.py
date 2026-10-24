name = "skynet terminator"
print(name)
print(name.title())
"""The title command changes the first letters of the words in the string to uppercase"""

print(name.upper())
"""uppper changes all the letters to uppercase"""

name = "SKYNET terminator"
print(name.lower())
"""lower changes all the letters to lowercase"""

first_name = "nathan"
last_name = "corradi"
full_name = f"{first_name} {last_name}"
print(full_name)
"""The (F) is the format command, it allows us to work with variables instead of the strings in the variable"""

print(f"Hello, {full_name.title()}!")
"""We can use methods to add a hello to the beginning of the message and add the title command as well"""

message = f"hello, {full_name.title()}!"
print(message)
"""Now everything as been shrunk down into a single variable to make it easier to understand on our end"""

prong_lang = ' python ' #variable prong_lang stores the current programming that we are using 
print(prong_lang) #printstatement that will print content of variable prong_lang to the user application layer
prong_lang.rstrip()
prong_lang.lstrip()
prong_lang.strip()
"""(.rstrip) removes the space at the back fo the variable, (.lstrip) removes the space at the front of the variable, (.strip) removes both spaces in the variable."""
"""To see you have to go on control panel because the variables aren't very complex"""

#this part of the code takes the values form sensor bla sand bla 
#conversts the signal from volt to degrees celcius and print it to 
#the UI
#above is examples of commenting


