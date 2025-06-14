'''
write a python program to read a string from user
print the count of uppercase vowels
print the count of lowercase vowels
print the count of uppercase consonants
print the count of lowercase consonants
'''
Str=input("Enter the String:")
U_vowels,L_vowels,U_consonants,L_consonants=0,0,0,0
for ch in Str:
    if(ch.isalpha() and ch.isupper()):
        if ch in 'AEIOU':
            U_vowels+=1
        else:
            U_consonants+=1
    if(ch.isalpha() and ch.islower()):
        if ch in 'aeiou':
            L_vowels+=1
        else:
            L_consonants+=1
print(f"Lower case Vowel Count:{L_vowels}")
print(f"Upper case Vowel Count:{U_vowels}")
print(f"Lower case Consonants Count:{L_consonants}")
print(f"Upper case Consonants Count:{U_consonants}")


Str=input("Enter the String:")
U_vowels,L_vowels,U_consonants,L_consonants=0,0,0,0
for ch in Str:
    if(ch>='A' and ch<='Z'):
        if ch in 'AEIOU':
            U_vowels+=1
        else:
            U_consonants+=1
    if(ch>='a' and ch<='z'):
        if ch in 'aeiou':
            L_vowels+=1
        else:
            L_consonants+=1
print(f"Lower case Vowel Count:{L_vowels}")
print(f"Upper case Vowel Count:{U_vowels}")
print(f"Lower case Consonants Count:{L_consonants}")
print(f"Upper case Consonants Count:{U_consonants}")

