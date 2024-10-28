# STRING SLICING REFERENCE

print('Specific Position:')
print("hello"[0])
print("hello"[1])
print("hello"[2])
print("hello"[3])
print("hello"[4])
print("----------------------------------------------------")
print("Output last character:")
print("hello"[-1])
print("----------------------------------------------------")
print('Output start position and remaining characters:')
print("hello"[0:]) # 0 and remaining
print("hello"[1:]) # 1 and remaining
print("hello"[2:]) # 2 and remaining
print("hello"[3:]) # and so on...
print("hello"[4:])
print("hello"[5:])
print("----------------------------------------------------")
print('Implicit 0 and the rest of the characters:')
print("hello"[:0]) # print from 0 to 0 so just 
print("hello"[:1]) # print from 0 to 2 
print("hello"[:2]) # print from 0 to 3
print("hello"[:3]) # and so on...
print("hello"[:4])
print("hello"[:5])
print("----------------------------------------------------")
print("Output only 'll' (position 2 up to but not including 4):")
print("hello"[2:4]) # This works kind of linke a range.
print("----------------------------------------------------")
print("string index out of range error")
print("hello"[20])
