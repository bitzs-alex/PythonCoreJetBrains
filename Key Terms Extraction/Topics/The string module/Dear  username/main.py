import string

# put your code here
template = string.Template("Dear $user! It was really nice to meet you."
                           + " Hopefully, you have a nice day! See you soon, $user!")
print(template.substitute(user=input().strip()))
