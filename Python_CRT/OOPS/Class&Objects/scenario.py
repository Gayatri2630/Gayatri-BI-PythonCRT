'''
scenario:
You have attended a skill development Training Program for 15 Days on Python Programming Language
Task:
Write a Python Program to give Detailed report of 15 days python
training which includes
1.Day
2.Topics Covered
3.Efficiency(Rate of Efficiiency & grip on topics learnt on a scaleof 5)
4.Number of Assignment Questions Sloved
5.Number of Hackerrank Questions Solved
6.Ratings Achieved on Hackerank on that particular day
7.Certifications Completed(includeing name of certificates)
8.Duration of class
9.Rate the Session on scale of 5 where 
    i) 1-being worst
    ii) 2-being bad
    iii) 3-being average
    iv) 4-being good 
    v) 5-being best
'''
class Report():
    def __init__(self,day,topics,efficiency,assigques,hackerankques,ratings,duration,rate):
        self.Day=day
        self.Topics=topics
        self.Efficiency=efficiency
        self.AssigQues=assigques
        self.HackerankQues=hackerankques
        self.Ratings=ratings
        self.Duration=duration
        self.Rate=rate
def Display_report(self):
    print("15 Days Report")
    print(f"Day:{self.Day}")
    print(f"Topics Covered:{self.Topics}")
    print(f"Efficiency(Rate of Efficiiency & grip on topics learnt on a scale of 5):{self.Efficiency}")
    print(f"NUmber of Assignment Questions Solved:{self.AssigQues}")
    print(f"Number of Hackerrank Questions Solved:{self.HackerankQues}")
    print(f"Ratings Achieved On Hackerrank On that Particular Day:{self.Ratings}")
    print(f"Duration of class:{self.Duration}")
    print(f"Rate the Session on scale of 5:{self.Rate}")
R1=Report(1,"Basics of Python",4,30,10,3,"3 hours","Average")
R2=Report(2,"Variables",4,35,15,4,"3 hours","Good")
R3=Report(3,"Operators",4,35,15,4,"3 hours","Average")
R4=Report(4,"Data Types",4,35,15,4,"3 hours","Average")
R5=Report(5,"Seq Data Types",4,35,15,4,"3 hours","Average")
R6=Report(6,"Sets",4,35,15,4,"3 hours","Good")
R7=Report(7,"Lists",4,35,15,4,"3 hours","Average")
R8=Report(8,"Strings",4,35,15,4,"3 hours","Average")
R9=Report(9,"Tuples",4,35,15,4,"3 hours","Average")
R10=Report(10,"Dictionary",4,35,15,4,"3 hours","Good")
R11=Report(11,"Functions",4,35,15,4,"3 hours","Average")
R12=Report(12,"OOPS",4,35,15,4,"3 hours","Average")
R13=Report(13,"Pillars of OOPS",4,35,15,4,"3 hours","Average")
R14=Report(14,"Class & Objects",4,35,15,4,"6 hours","Good")
R15=Report(15,"Revision",4,35,15,4,"3 hours","Average")
Display_report(R1)
Display_report(R2)
Display_report(R3)
Display_report(R4)
Display_report(R5)
Display_report(R6)
Display_report(R7)
Display_report(R8)
Display_report(R9)
Display_report(R10)
Display_report(R11)
Display_report(R12)
Display_report(R13)
Display_report(R14)
Display_report(R15)


