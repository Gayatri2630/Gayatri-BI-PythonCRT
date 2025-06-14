Str=input("Enter the String:")
new_str=""
for ch in Str:
    if ch in 'aeiou':
        new_str+='0'
    else:
        new_str+=i
print(new_str)


