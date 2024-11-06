age = 101

if age < 4:
    print("Admission is $0.00") 
elif age < 18: 
    print("Admission is $25.00")
elif age > 60:
    print("Admission is $35.00")
elif age > 100:
    print("Admission is $0 and you get a free beer!") # here is the bug, it is caused because both "age > 60" and "age > 100" are true, but because "age > 60" is read first, that is what the program does.
else:
    print("Admission is $40.00")
    