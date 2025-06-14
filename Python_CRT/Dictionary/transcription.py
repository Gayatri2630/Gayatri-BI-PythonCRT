'''transription simulation
turn DNA into RNA by replacing every T with U
write a loop to convert a DNA string to its RNA form'''
sequence=input("Enter the DNA string:")
for i in sequence:
    seq=sequence.replace('T','U')
print(f"Converted String:{seq}")