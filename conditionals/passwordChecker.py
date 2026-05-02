
password = "123456"

if(len(password)<6):
 strength = "Password is weak"
elif(len(password)<=10):
    strength = "Password is medium"

else: strength = "Password is strong"

print(strength)