'''compare two strings of the same length and print the positions(indices)
where the sequence differ.'''
seq1=input("Enter the first sequence:")
seq2=input("Enter the second sequence:")
print(seq1)
print(seq2)
List=[]
if(len(seq1)==len(seq2)):
    for i in range(len(seq1)):
        if seq1[i] not in seq2[i]:
             List.append(i)
print(List)

