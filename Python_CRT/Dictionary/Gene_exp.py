'''based on the value ,you need to label each gene as:
"Underexpressed"(<5)
"Normal"(5 to 15)
"Overexpressed"(>15)
Look through the list and assign the correct label to each number'''
n=int(input("Enter the Count of data:"))
Gene=[]
for i in range(n):
    temp=float(input("Enter the Elements:"))
    Gene.append(temp)
print(f"User Entered List:{Gene}")
Exp_result=[]
for i in Gene:
    if i<5:
        Exp_result.append("Underexpressed")
    elif i>=5 and i<=15:
        Exp_result.append("Normal")
    else:
        Exp_result.append("Overexpressed")
print(Exp_result)
        