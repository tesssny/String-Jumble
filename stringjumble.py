"""
stringjumble.py
Author: Tess Snyder
Credit: Avery Wallis, Adam Glueck, Dan the Man

Assignment:

The purpose of this challenge is to gain proficiency with 
manipulating lists.

Write and submit a Python program that accepts a string from 
the user and prints it back in three different ways:

* With all letters in reverse.
* With words in reverse order, but letters within each word in 
  the correct order.
* With all words in correct order, but letters reversed within 
  the words.

Output of your program should look like this:

Please enter a string of text (the bigger the better): There are a few techniques or tricks that you may find handy
You entered "There are a few techniques or tricks that you may find handy". Now jumble it:
ydnah dnif yam uoy taht skcirt ro seuqinhcet wef a era erehT
handy find may you that tricks or techniques few a are There
erehT era a wef seuqinhcet ro skcirt taht uoy yam dnif ydnah
"""
text=input("Please enter a string of text (the bigger the better): ")
l=int(len(text))

for x in range(-1,-l-1,-1):
     print(text[x], end="")

print("\n")

words=text.split(' ')
 
f=list(reversed(words))
for w in f:
    print(w, end=" ")

print("\n")

for x in f:
    g=0
    while g < len(x):
        e=str(x[len(x)-g-1])
        print("{0}".format(e), end="")
        g=g+1
    print(" ", end="")

