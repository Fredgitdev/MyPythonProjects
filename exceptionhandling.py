#print(number)

#You can't print number since it has no value,
# yes it is a variable but it lacks a value

#to check if the block has an error, create a try block

try:
    print(number)
#PRINT THE MESSAGE IF TRUE, THERE IS AN ERROR
except:
    print("WARNING, AN ERROR HAS OCCURRED")

#YOU CAN NEVER DIVIDE A NUMBER BY 0

num1 = 39
num2 = 0

try:
    print(num1 / num2)
except:
    print("WARNING, ANOTHER ERROR, A ZERO DIVISION ERROR HAS OCCURRED")
#finally block gets excecuted no matter what
finally:
    print("Success")
    


