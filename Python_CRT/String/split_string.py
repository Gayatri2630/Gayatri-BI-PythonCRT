Str=input("Enter the String:")
length=len(Str)
part_size=length//3
part1=''
part3=''
i=0
while i<part_size:
    part1+=Str[i]
    i+=1
part2=''
j=0
while j<part_size:
    part2+=Str[i]
    i+=1
    j+=1
k=0
while k<part_size:
    part3+=Str[i]
    i+=1
    k+=1
print(f"Part 1:{part1}")
print(f"Part 2:{part2}")
print(f"Part 3:{part3}")