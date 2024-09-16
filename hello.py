#! /usr/bin/env python

""" multi-language
depending on the language configured in the environment, the program displays the correponding message. 

make sure the LANG variable is properly configured

execution:
    python3 (name file)
    ./name file

"""

current_language = "it_IT"

msg = "Hello, World!"

if current_language == "pt_BR":
    msg = "Olá, Mundo!"

elif current_language == "it_IT":
    msg = "Ciao, Monda!"

print (msg)

