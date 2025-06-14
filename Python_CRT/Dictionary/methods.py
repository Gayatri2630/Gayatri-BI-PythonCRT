JobRole={101:'Full Stack Developer',102:'Data Engineer',103:'Data Analyst',104:'Data Scientist'}
print(JobRole)
JobRole[105]='Cloud Enginner'
print(JobRole)
JobRole[106]='Web Developer'
print(JobRole)
#removing of element from dictionary
Job=JobRole.pop(101)
print(Job)
print(JobRole)
del JobRole[102]
print(JobRole)
#len():returns the number of key-value pairs in dictionary
print(len(JobRole))
#keys():returns a list of all the keys in a dictionary
print(JobRole.keys())
#values():returns a list of all the values in a dictionary
print(JobRole.values())
#items(): returns a list of key-value pairs as tuples in a dictionary
print(JobRole.items())
#copy():returns the copy of the dictionary
b=JobRole.copy()
print(b)
#update():returns one dictionary in another dictionary
Dict1={1:'a',2:'b',3:'c',4:'d'}
print(Dict1)
Dict2={5:'e',6:'f',7:'g'}
print(Dict2)
Dict1.update(Dict2)
print(Dict1)
