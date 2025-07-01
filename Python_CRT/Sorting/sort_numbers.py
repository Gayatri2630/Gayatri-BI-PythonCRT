'''
Problem:
You ar given an array of integers representing stduent score.
Your task is to sort the array in ascending order using basic soring alogrithm
(Bubble sort/Selection Sort/Insertion sort)

Input:
An integer n-number of students
An array of n integers - the scores

Output:
Sorted array of scores in ascending order
'''
Arr=[55,80,40,62,57,45]
print(f"Scores:{Arr}")
for i in range(len(Arr)):
    for j in range(len(Arr)-1):
        if (Arr[j]>Arr[j+1]):
            Arr[j],Arr[j+1]=Arr[j+1],Arr[j]
print(f"Sorted Scores:{Arr}")