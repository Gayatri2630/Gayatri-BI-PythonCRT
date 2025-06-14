'''Some Dna sequences are palindromic,meaning they match their reverse complement.
Find the reverse complement(A<->T,C<->G)
and see if it matches the original'''
complement={'A':'T','C':'G'}
seq=input("Enter the Sequence:").upper()
comp=''
for base in seq:
    if base in complement:
        comp+=complement[base]
    else:
        comp+=base
t=comp
rev_comp=comp[::-1]
if rev_comp==comp:
    print("True")
else:
    print("False")