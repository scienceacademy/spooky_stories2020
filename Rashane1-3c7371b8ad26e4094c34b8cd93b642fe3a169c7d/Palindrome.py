#ask for user's input in string:

string = str(input("Enter string: "))

#return the output as reverse:

s = (string[::-1])
print (s)

#if statement to clarify if it is palindrome.

if string == s:
    print ("TEXT: " + (s))
    print ("PALINDROME")
elif string != s:
    print ("TEXT: " + (s))
    print ("NOT PALINDROME")