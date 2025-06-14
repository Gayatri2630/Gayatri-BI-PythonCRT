'''
candidate_name:Tuple of candidate name
interview_times: list of integers
1.takes the current time(intger) as input from the user
2.display all candidates scheluded after that time
3.if no candidates are scheluded after.print"ALL INTERVIEWS ARE COMPLETE"
Input Format:
  enter current time(0-23):13
output format:
'''
candidate_name=('Aruna','Kruthika','Dharani','Anusha','Goppali','Alice','Ravi')
interview_time=[9,10,11,12,13,14,15]
n=input("Enter Current time(0-23):")
if n.isdigit():
  current_time=int(n)
  found=False
  print("Candidates scheduled after current time:")
  for i in range(len(interview_time)):
    if interview_time[i]>current_time:
      print(candidate_name[i],"-",interview_time[i])
      found=True
  if not found:
    print("All Interviews are Completed")
else:
  print("Invalid time.")

