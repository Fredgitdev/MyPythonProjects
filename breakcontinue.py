#Break statements - Used to exit a loop
#Printing values 20-25 but when at 23, exit


num = 20
while num <=25:
    print(num)
    if num == 23:
        break
    num += 1


#Continue statement - skips a loop


devices = ["laptop", "phone", "tablet"]
for x in devices:
    if x == "phone":
        continue
    print(x)












