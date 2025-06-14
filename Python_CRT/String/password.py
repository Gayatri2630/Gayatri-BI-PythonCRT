Str=input("Enter the Password:")
U_case,L_case,D_case,S_case=0,0,0,0
if(len(Str)>=8):
    for i in Str:
        if(i.islower()):
            U_case+=1
        if(i.isupper()):
            L_case+=1
        if(i.isdigit()):
            D_case+=1
        if(i=='@' or i=='$' and i=='_'):
            S_case+=1
if(U_case>=1 and L_case>=1 and D_case>=1 and S_case>=1 and U_case+L_case+D_case+S_case==len(Str)):
    print("Valid Password")
else:
    print("Invalid Password")
