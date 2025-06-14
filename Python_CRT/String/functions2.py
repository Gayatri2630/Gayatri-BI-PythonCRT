Str=input("Enter the String:")
Uppercase_Alpha=0
Lowercase_Alpha=0
Numeric=0
Special_char=0
for ch in Str:
    if ch.isupper():
        Uppercase_Alpha+=1
    elif ch.islower():
        Lowercase_Alpha+=1
    elif ch.isdigit():
        Numeric+=1
    else:
        Special_char+=1
print(f"Count of Upper case Letters:{Uppercase_Alpha}")
print(f"Count of Lower case Letters:{Lowercase_Alpha}")
print(f"Count of Numeric Values:{Numeric}")
print(f"Count of Special Characters:{Special_char}")
