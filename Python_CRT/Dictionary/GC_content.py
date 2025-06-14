sequence=input("Enter the Sequence:")
total_base=len(sequence)
G=0
for i in sequence:
    if i in "GC":
        G+=1
gc_content=(G/total_base)*100
print(f"GC content:{gc_content:.2f}")
if gc_content<=40:
    print("Classfication: Low GC")
elif gc_content>40 and gc_content<=60:
    print("Classification: Moderate GC")
else:
    print("Classification: High GC")