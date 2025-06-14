'''write a program that
checks if the string has only valid bases(A,T,G,C)
then count how many of each base there are.'''
base=input("Enter the Sample Base Value:")
a_count,t_count,c_count,g_count=0,0,0,0
for i in base:
    if i in "ATCG":
        if i=='A':
            a_count+=1
        elif i=='T':
            t_count+=1
        elif i=='G':
            g_count+=1
        elif i=='C':
            c_count+=1
new_base={'A':a_count,'T':t_count,'G':g_count,'C':c_count}
print(new_base)
#Another method
sequence=input("Enter the Sequence:")
base_count={'A':sequence.count('A'),'T':sequence.count('T'),'G':sequence.count('G'),'C':sequence.count('C')}
print(base_count)




